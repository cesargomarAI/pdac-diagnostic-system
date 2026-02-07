import joblib
import pandas as pd
import informe_medico

def diagnostico_interactivo():
    try:
        model = joblib.load('ia_cancer_pancreas.joblib')
        
        print("\n" + "="*60)
        print("🏥 SISTEMA DE APOYO AL DIAGNÓSTICO PRECOZ - PDAC v2.0")
        print("="*60)
        
        age = float(input("1. Edad del paciente: "))
        creatinine = float(input("2. Creatinina (mg/dl): "))
        lyve1 = float(input("3. LYVE1 (ng/ml): "))
        reg1b = float(input("4. REG1B (ng/ml): "))
        tff1 = float(input("5. TFF1 (ng/ml): "))

        # Normalización
        l_n, r_n, t_n = lyve1/creatinine, reg1b/creatinine, tff1/creatinine
        
        # Nuevas características de Segundo Orden
        data_input = pd.DataFrame([[
            age, l_n, r_n, t_n,
            l_n * r_n,              # LYVE1_REG1B
            t_n / (r_n + 1),        # TFF1_REG1B
            (l_n * t_n) / age       # COMBO_TRES
        ]], columns=['age', 'LYVE1_norm', 'REG1B_norm', 'TFF1_norm', 'LYVE1_REG1B', 'TFF1_REG1B', 'COMBO_TRES'])

        probabilidades = model.predict_proba(data_input)[0]
        clases = ['Sano', 'Benigno', 'Cáncer']
        
        print("\n" + "-"*40)
        print("📋 RESULTADOS v2.0 (ANÁLISIS DE CORRELACIÓN):")
        for i, clase in enumerate(clases):
            print(f"   > {clase:12}: {probabilidades[i]*100:6.2f}%")
        
        riesgo = probabilidades[2] * 100
        print("-" * 40)
        if riesgo > 50: print("🛑 ALERTA: ALTO RIESGO.")
        elif riesgo > 20: print("⚠️ AVISO: RIESGO MODERADO.")
        else: print("✅ INFO: RIESGO BAJO.")
        
        if input("\n¿Generar PDF? (s/n): ").lower() == 's':
            informe_medico.generar_pdf({'age':age,'creatinine':creatinine,'lyve1':lyve1,'reg1b':reg1b,'tff1':tff1}, probabilidades)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    diagnostico_interactivo()
