import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
import informe_medico
import os

st.set_page_config(page_title="PDAC Predictor v2.0", page_icon="🏥", layout="wide")

st.title("🏥 Sistema de Apoyo al Diagnóstico - PDAC")
st.markdown("---")

# Inicializar estados de memoria si no existen
if 'prediccion_lista' not in st.session_state:
    st.session_state.prediccion_lista = False
    st.session_state.probs = None
    st.session_state.datos_paciente = None

# Barra lateral
st.sidebar.header("📥 Datos del Laboratorio")
age = st.sidebar.slider("Edad del paciente", 20, 95, 50)
creatinine = st.sidebar.number_input("Creatinina (mg/dl)", 0.1, 3.0, 1.0)
lyve1 = st.sidebar.number_input("LYVE1 (ng/ml)", 0.0, 30.0, 5.0)
reg1b = st.sidebar.number_input("REG1B (ng/ml)", 0.0, 1000.0, 200.0)
tff1 = st.sidebar.number_input("TFF1 (ng/ml)", 0.0, 3000.0, 500.0)

if st.sidebar.button("🚀 REALIZAR ANÁLISIS"):
    # Procesamiento
    l_n, r_n, t_n = lyve1/creatinine, reg1b/creatinine, tff1/creatinine
    data_input = pd.DataFrame([[
        age, l_n, r_n, t_n, l_n * r_n, t_n / (r_n + 1), (l_n * t_n) / age
    ]], columns=['age', 'LYVE1_norm', 'REG1B_norm', 'TFF1_norm', 'LYVE1_REG1B', 'TFF1_REG1B', 'COMBO_TRES'])

    # Predicción
    model = joblib.load('ia_cancer_pancreas.joblib')
    st.session_state.probs = model.predict_proba(data_input)[0]
    st.session_state.datos_paciente = {'age':age,'creatinine':creatinine,'lyve1':lyve1,'reg1b':reg1b,'tff1':tff1}
    st.session_state.prediccion_lista = True

# Si hay una predicción en memoria, mostrarla
if st.session_state.prediccion_lista:
    col1, col2 = st.columns([2, 1])
    probs = st.session_state.probs
    
    with col1:
        st.subheader("📊 Perfil de Riesgo Bioquímico")
        df_res = pd.DataFrame({'Estado': ['Sano', 'Benigno', 'Cáncer'], 'Probabilidad': probs})
        fig = px.pie(df_res, values='Probabilidad', names='Estado', hole=0.4,
                     color='Estado', color_discrete_map={'Sano':'#27ae60','Benigno':'#2980b9','Cáncer':'#c0392b'})
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        riesgo = probs[2] * 100
        st.metric("Probabilidad de Cáncer", f"{riesgo:.2f}%")
        if riesgo > 50: st.error("🛑 **ALERTA: ALTO RIESGO**")
        elif riesgo > 20: st.warning("⚠️ **AVISO: RIESGO MODERADO**")
        else: st.success("✅ **INFO: RIESGO BAJO**")

    st.markdown("---")
    # BOTÓN DE GENERACIÓN CORREGIDO
    if st.button("📄 GENERAR INFORME CLÍNICO OFICIAL"):
        nombre_archivo = informe_medico.generar_pdf(st.session_state.datos_paciente, probs)
        if os.path.exists(nombre_archivo):
            st.success(f"✅ Informe generado: **{nombre_archivo}**")
            with open(nombre_archivo, "rb") as f:
                st.download_button(label="⬇️ Descargar PDF", data=f, file_name=nombre_archivo, mime="application/pdf")
else:
    st.info("👋 Introduzca los datos y pulse 'Realizar Análisis'.")
