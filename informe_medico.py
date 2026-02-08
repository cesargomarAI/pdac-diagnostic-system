from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def generar_pdf(datos_paciente, probabilidades, idioma="Spanish"):
    # Diccionario de traducciones para el PDF
    texts = {
        "Spanish": {
            "filename": "Informe_IA_PDAC",
            "header": "SISTEMA DE APOYO AL DIAGNÓSTICO PRECOZ (PDAC-v2)",
            "data_title": "DATOS DEL ANÁLISIS:",
            "date": "Fecha del estudio:",
            "age": "Edad:",
            "years": "años",
            "markers_title": "NIVELES DE BIOMARCADORES DETECTADOS:",
            "ai_result": "RESULTADO DE LA IA",
            "high": "RIESGO ALTO",
            "mid": "RIESGO MODERADO",
            "low": "RIESGO BAJO",
            "rec_title": "RECOMENDACIÓN CLÍNICA:",
            "rec_high": "Priorizar estudio por imagen (TAC/RMN) y derivación urgente a Oncología.",
            "rec_mid": "Seguimiento estrecho y repetición de analítica en 90 días.",
            "rec_low": "No se observan patrones de sospecha. Continuar cribado estándar.",
            "note1": "* Este informe es una herramienta de apoyo basada en el estudio Debernardi et al. (2020).",
            "note2": "* No constituye un diagnóstico definitivo. Debe ser validado por un especialista."
        },
        "English": {
            "filename": "AI_Report_PDAC",
            "header": "EARLY DIAGNOSTIC SUPPORT SYSTEM (PDAC-v2)",
            "data_title": "ANALYSIS DATA:",
            "date": "Study date:",
            "age": "Age:",
            "years": "years",
            "markers_title": "DETECTED BIOMARKER LEVELS:",
            "ai_result": "AI ANALYSIS RESULT",
            "high": "HIGH RISK",
            "mid": "MODERATE RISK",
            "low": "LOW RISK",
            "rec_title": "CLINICAL RECOMMENDATION:",
            "rec_high": "Prioritize imaging (CT/MRI) and urgent referral to Oncology.",
            "rec_mid": "Close follow-up and repeat laboratory tests in 90 days.",
            "rec_low": "No suspicious patterns observed. Continue standard screening.",
            "note1": "* This report is a support tool based on the Debernardi et al. (2020) study.",
            "note2": "* It does not constitute a definitive diagnosis. It must be validated by a specialist."
        }
    }

    t = texts[idioma]
    nombre_archivo = f"{t['filename']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    # --- Encabezado ---
    c.setFillColor(colors.darkblue)
    c.rect(0, height - 80, width, 80, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 16) # Bajamos un poco el tamaño para que quepa el inglés
    c.drawString(50, height - 50, t["header"])
    
    # --- Datos del Paciente ---
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 120, t["data_title"])
    c.setFont("Helvetica", 11)
    c.drawString(70, height - 140, f"{t['date']} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    c.drawString(70, height - 155, f"{t['age']} {datos_paciente['age']} {t['years']}")
    c.drawString(70, height - 170, f"Creatinine: {datos_paciente['creatinine']} mg/dl")
    
    # --- Resultados de Biomarcadores ---
    c.line(50, height - 185, 550, height - 185)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 205, t["markers_title"])
    c.setFont("Helvetica", 11)
    c.drawString(70, height - 225, f"LYVE1: {datos_paciente['lyve1']} ng/ml")
    c.drawString(70, height - 240, f"REG1B: {datos_paciente['reg1b']} ng/ml")
    c.drawString(70, height - 255, f"TFF1: {datos_paciente['tff1']} ng/ml")
    
    # --- Evaluación de la IA ---
    c.setFillColor(colors.lightgrey)
    c.rect(50, height - 380, 500, 100, fill=1)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - 300, t["ai_result"])
    
    riesgo = probabilidades[2] * 100
    c.setFont("Helvetica-Bold", 18)
    if riesgo > 50:
        c.setFillColor(colors.red)
        texto_riesgo = t["high"]
        rec = t["rec_high"]
    elif riesgo > 20:
        c.setFillColor(colors.orange)
        texto_riesgo = t["mid"]
        rec = t["rec_mid"]
    else:
        c.setFillColor(colors.green)
        texto_riesgo = t["low"]
        rec = t["rec_low"]
    
    c.drawCentredString(width/2, height - 330, f"{texto_riesgo} ({riesgo:.2f}%)")
    
    # --- Recomendaciones ---
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 410, t["rec_title"])
    c.setFont("Helvetica", 11)
    c.drawString(70, height - 430, rec)
    
    # --- Nota de Rigor Científico ---
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(50, 50, t["note1"])
    c.drawString(50, 40, t["note2"])
    
    c.save()
    return nombre_archivo