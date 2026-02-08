# 🏥 PDAC Diagnostic Support System (v2.0)
**Advanced AI for Early Pancreatic Cancer Detection**
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green)
![Streamlit](https://img.shields.io/badge/Deployment-Live%20App-red)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

### 🚀 Access the live APP here:
👉 **[CLICK TO OPEN THE INTERACTIVE APP](https://pdac-diagnostic-system-7jyt3cxbcaqwmravjnog5b.streamlit.app/)**

---

### 🧬 Project Summary
This system is a state-of-the-art **Applied AI** solution designed for the early detection of Pancreatic Ductal Adenocarcinoma (PDAC). The tool enables healthcare professionals to upload or input urinary biomarkers and receive an instant diagnostic probability supported by Machine Learning.

### 🔬 Scientific Basis
The model is based on the research by **Debernardi et al. (2020)**, utilizing levels of:
* **LYVE1**, **REG1B**, and **TFF1** (Urinary biomarkers).
* **Creatinine** (for normalization).
* **Patient Age**.

## 🛠️ Tecnologic Stack 
**Multilingual Interface:** Full support for English and Spanish.
* **Core Engine:** Scikit-Learn (Random Forest classification model).
* **Feature Engineering:** Implementation of second-order ratios to capture non-linear interactions between biomarkers (LYVE1, REG1B, TFF1).
* **Interface:** Interactive dashboard built with **Streamlit**.
* **Analytics:** Real-time data visualization using **Plotly**.
* **Documentación:** Automated clinical report generation in **PDF** format.

## 🧠 Technical Innovation
The key strength of this model lies not only in prediction, but in **biochemical normalization**. The system automatically computes protein-to-creatinine ratios, enabling reliable differentiation between benign inflammation (pancreatitis) and early-stage cancer, thereby significantly reducing false positives.

## 📦 Execution and Deployment
The project is containerized and production-ready:

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

### 🧬 Resumen del Proyecto
Este sistema es una solución de **Applied AI** de vanguardia diseñada para la detección temprana del Adenocarcinoma Ductual Pancreático (PDAC). La herramienta permite a los profesionales de la salud cargar o introducir biomarcadores urinarios y obtener una probabilidad diagnóstica instantánea respaldada por Machine Learning.

### 🔬 Base Científica
El modelo se basa en el estudio de **Debernardi et al. (2020)**, utilizando los niveles de:
* **LYVE1, REG1B y TFF1** (Biomarcadores en orina).
* **Creatinina** (para normalización).
* **Edad del paciente**.

## 🛠️ Stack Tecnológico
**Interfaz Multilingüe:** Soporte completo en Inglés y Español.
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


**Desarrollado por Cesar Gomar - Applied AI Engineer**
<img width="1024" height="1024" alt="logo" src="https://github.com/user-attachments/assets/fffcc24d-bcf3-4cd9-9c40-9d938adb59c4" />

