import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
import informe_medico
import os
import numpy as np

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="PDAC Predictor v2.0", page_icon="🏥", layout="centered")

# --- DICCIONARIO DE IDIOMAS ---
texts = {
    "English": {
        "title": "🏥 PDAC Diagnostic Support System",
        "subtitle": "Advanced AI for early pancreatic cancer detection",
        "lang_label": "Choose Language / Seleccione Idioma",
        "header_lab": "📥 Laboratory Data",
        "age": "Patient Age",
        "creatinine": "Creatinine (mg/dl)",
        "lyve1": "LYVE1 (ng/ml)",
        "reg1b": "REG1B (ng/ml)",
        "tff1": "TFF1 (ng/ml)",
        "btn_run": "🚀 RUN ANALYSIS",
        "results_title": "📊 Biochemical Risk Profile",
        "prob_label": "Cancer Probability",
        "state_labels": ['Healthy', 'Benign', 'Cancer'],
        "alert_high": "🛑 **ALERT: HIGH RISK**",
        "alert_mid": "⚠️ **NOTICE: MODERATE RISK**",
        "alert_low": "✅ **INFO: LOW RISK**",
        "btn_report": "📄 GENERATE OFFICIAL CLINICAL REPORT",
        "btn_download": "⬇️ Download PDF",
        "info_wait": "👋 Enter data and press 'Run Analysis'.",
        "footer": "Applied AI Engineer: Cesar"
    },
    "Spanish": {
        "title": "🏥 Sistema de Apoyo al Diagnóstico - PDAC",
        "subtitle": "IA avanzada para la detección precoz de cáncer de páncreas",
        "lang_label": "Seleccione Idioma / Choose Language",
        "header_lab": "📥 Datos del Laboratorio",
        "age": "Edad del paciente",
        "creatinine": "Creatinina (mg/dl)",
        "lyve1": "LYVE1 (ng/ml)",
        "reg1b": "REG1B (ng/ml)",
        "tff1": "TFF1 (ng/ml)",
        "btn_run": "🚀 REALIZAR ANÁLISIS",
        "results_title": "📊 Perfil de Riesgo Bioquímico",
        "prob_label": "Probabilidad de Cáncer",
        "state_labels": ['Sano', 'Benigno', 'Cáncer'],
        "alert_high": "🛑 **ALERTA: ALTO RIESGO**",
        "alert_mid": "⚠️ **AVISO: RIESGO MODERADO**",
        "alert_low": "✅ **INFO: RIESGO BAJO**",
        "btn_report": "📄 GENERAR INFORME CLÍNICO OFICIAL",
        "btn_download": "⬇️ Descargar PDF",
        "info_wait": "👋 Introduzca los datos y pulse 'Realizar Análisis'.",
        "footer": "Applied AI Engineer: Cesar"
    }
}

# --- SELECTOR DE IDIOMA CENTRAL ---
sel_lang = st.selectbox("", ["Spanish", "English"], label_visibility="collapsed")
t = texts[sel_lang]

# --- TÍTULOS ---
st.markdown(f"<h1 style='text-align: center;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: gray;'>{t['subtitle']}</p>", unsafe_allow_html=True)
st.markdown("---")

# Inicializar estados de memoria
if 'prediccion_lista' not in st.session_state:
    st.session_state.prediccion_lista = False
    st.session_state.probs = None
    st.session_state.datos_paciente = None

# --- ENTRADA DE DATOS (CENTRAL & RESPONSIVE) ---
st.subheader(t["header_lab"])
col_a, col_b = st.columns(2)

with col_a:
    age = st.number_input(t["age"], 20, 95, 50)
    creatinine = st.number_input(t["creatinine"], 0.1, 3.0, 1.0, format="%.2f")

with col_b:
    lyve1 = st.number_input(t["lyve1"], 0.0, 30.0, 5.0, format="%.2f")
    reg1b = st.number_input(t["reg1b"], 0.0, 1000.0, 200.0, format="%.2f")

tff1 = st.number_input(t["tff1"], 0.0, 3000.0, 500.0, format="%.2f")

st.write("")
if st.button(t["btn_run"], use_container_width=True, type="primary"):
    # Lógica de Ingeniería de Características (Manteniendo tu fórmula original)
    l_n, r_n, t_n = lyve1/creatinine, reg1b/creatinine, tff1/creatinine
    data_input = pd.DataFrame([[
        age, l_n, r_n, t_n, l_n * r_n, t_n / (r_n + 1), (l_n * t_n) / age
    ]], columns=['age', 'LYVE1_norm', 'REG1B_norm', 'TFF1_norm', 'LYVE1_REG1B', 'TFF1_REG1B', 'COMBO_TRES'])

    # Predicción
    try:
        model = joblib.load('ia_cancer_pancreas.joblib')
        st.session_state.probs = model.predict_proba(data_input)[0]
        st.session_state.datos_paciente = {'age':age,'creatinine':creatinine,'lyve1':lyve1,'reg1b':reg1b,'tff1':tff1}
        st.session_state.prediccion_lista = True
    except Exception as e:
        st.error(f"Error: {e}")

# --- RESULTADOS ---
if st.session_state.prediccion_lista:
    st.markdown("---")
    st.subheader(t["results_title"])
    
    col1, col2 = st.columns([1.5, 1])
    probs = st.session_state.probs
    
    with col1:
        df_res = pd.DataFrame({'Estado': t["state_labels"], 'Probabilidad': probs})
        fig = px.pie(df_res, values='Probabilidad', names='Estado', hole=0.4,
                     color='Estado', color_discrete_map={t["state_labels"][0]:'#27ae60',
                                                       t["state_labels"][1]:'#2980b9',
                                                       t["state_labels"][2]:'#c0392b'})
        fig.update_layout(showlegend=True, margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        riesgo = probs[2] * 100
        st.metric(t["prob_label"], f"{riesgo:.2f}%")
        if riesgo > 50: st.error(t["alert_high"])
        elif riesgo > 20: st.warning(t["alert_mid"])
        else: st.success(t["alert_low"])

    st.write("")
    if st.button(t["btn_report"], use_container_width=True):
       # Pasamos 'sel_lang' que es la variable donde guardamos el idioma elegido
        nombre_archivo = informe_medico.generar_pdf(st.session_state.datos_paciente, probs, sel_lang)
        if os.path.exists(nombre_archivo):
            st.success(f"✅ {nombre_archivo}")
            with open(nombre_archivo, "rb") as f:
                st.download_button(label=t["btn_download"], data=f, file_name=nombre_archivo, mime="application/pdf", use_container_width=True)
else:
    st.info(t["info_wait"])

# --- FOOTER & LOGO ---
st.write("")
st.divider()
col_f1, col_f2, col_f3 = st.columns([1, 2, 1])
with col_f2:
    st.image("logo.png", width=250)
    st.markdown(f"<p style='text-align: center; color: silver;'>{t['footer']}</p>", unsafe_allow_html=True)