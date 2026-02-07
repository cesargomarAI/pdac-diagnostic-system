# 🏥 PDAC Diagnostic Support System (v2.0)
<p align="center">
  <img src="logo.png" width="200">
</p>
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green)
![Streamlit](https://img.shields.io/badge/Deployment-Live%20App-red)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

### 🚀 Accede a la aplicación en vivo aquí:
👉 **[CLICK PARA ABRIR LA APP INTERACTIVA](https://pdac-diagnostic-system-7jyt3cxbcaqwmravjnog5b.streamlit.app/)**

---

### 🧬 Resumen del Proyecto
Este sistema es una solución de **Applied AI** de vanguardia diseñada para la detección temprana del Adenocarcinoma Ductual Pancreático (PDAC). La herramienta permite a los profesionales de la salud cargar o introducir biomarcadores urinarios y obtener una probabilidad diagnóstica instantánea respaldada por Machine Learning.

## 🛠️ Stack Tecnológico
* **Core Engine:** Scikit-Learn (Modelo de clasificación Random Forest).
* **Feature Engineering:** Implementación de **Ratios de Segundo Orden** para capturar interacciones no lineales entre biomarcadores (LYVE1, REG1B, TFF1).
* **Interface:** Dashboard interactivo con **Streamlit**.
* **Analytics:** Visualización de datos en tiempo real mediante **Plotly**.
* **Documentación:** Generación de informes clínicos automáticos en formato **PDF**.

## 🧠 Innovación Técnica
La clave de este modelo no es solo la predicción, sino la **normalización bioquímica**. El sistema calcula automáticamente la relación entre las proteínas y la creatinina, permitiendo diferenciar con éxito entre inflamaciones benignas (pancreatitis) y estadios tempranos de cáncer, reduciendo significativamente los falsos positivos.

## 📦 Ejecución y Despliegue
El proyecto está containerizado y listo para producción:

### Local (Conda/Venv):
\`\`\`bash
git clone https://github.com/cesargomarAI/pdac-diagnostic-system.git
pip install -r requirements.txt
streamlit run app.py
\`\`\`

### Docker:
\`\`\`bash
docker build -t pdac-sys .
docker run -p 8501:8501 pdac-sys
\`\`\`

---
**Desarrollado por Cesar - Applied AI Engineer**
