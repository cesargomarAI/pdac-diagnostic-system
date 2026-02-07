from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def generar_pdf(datos_paciente, probabilidades):
    nombre_archivo = f"Informe_IA_PDAC_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    # --- Encabezado ---
    c.setFillColor(colors.darkblue)
    c.rect(0, height - 80, width, 80, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "SISTEMA DE APOYO AL DIAGNÓSTICO PRECOZ (PDAC-v1)")
    
    # --- Datos del Paciente ---
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 120, "DATOS DEL ANÁLISIS:")
    c.setFont("Helvetica", 11)
    c.drawString(70, height - 140, f"Fecha del estudio: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    c.drawString(70, height - 155, f"Edad: {datos_paciente['age']} años")
    c.drawString(70, height - 170, f"Creatinina: {datos_paciente['creatinine']} mg/dl")
    
    # --- Resultados de Biomarcadores ---
    c.line(50, height - 185, 550, height - 185)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 205, "NIVELES DE BIOMARCADORES DETECTADOS:")
    c.setFont("Helvetica", 11)
    c.drawString(70, height - 225, f"LYVE1: {datos_paciente['lyve1']} ng/ml")
    c.drawString(70, height - 240, f"REG1B: {datos_paciente['reg1b']} ng/ml")
    c.drawString(70, height - 255, f"TFF1: {datos_paciente['tff1']} ng/ml")
    
    # --- Evaluación de la IA ---
    c.setFillColor(colors.lightgrey)
    c.rect(50, height - 380, 500, 100, fill=1)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, height - 300, "RESULTADO DE LA IA")
    
    riesgo = probabilidades[2] * 100
    c.setFont("Helvetica-Bold", 18)
    if riesgo > 50:
        c.setFillColor(colors.red)
        texto_riesgo = "RIESGO ALTO"
    elif riesgo > 20:
        c.setFillColor(colors.orange)
        texto_riesgo = "RIESGO MODERADO"
    else:
        c.setFillColor(colors.green)
        texto_riesgo = "RIESGO BAJO"
    
    c.drawCentredString(width/2, height - 330, f"{texto_riesgo} ({riesgo:.2f}%)")
    
    # --- Recomendaciones ---
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 410, "RECOMENDACIÓN CLÍNICA:")
    c.setFont("Helvetica", 11)
    if riesgo > 50:
        rec = "Priorizar estudio por imagen (TAC/RMN) y derivación urgente a Oncología."
    elif riesgo > 20:
        rec = "Seguimiento estrecho y repetición de analítica en 90 días."
    else:
        rec = "No se observan patrones de sospecha. Continuar cribado estándar."
    c.drawString(70, height - 430, rec)
    
    # --- Nota de Rigor Científico ---
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(50, 50, "* Este informe es una herramienta de apoyo basada en el estudio Debernardi et al. (2020).")
    c.drawString(50, 40, "* No constituye un diagnóstico definitivo. Debe ser validado por un especialista.")
    
    c.save()
    return nombre_archivo

print("Generador de Informes cargado con éxito.")
