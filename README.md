# 📊 Log & Incident Data Processor

Herramienta de análisis y tratamiento de datos orientada a auditoría de sistemas e incidencias de soporte IT, implementada con **Python** y **Pandas**.

## 📋 Funcionalidades
- **Extracción y Carga (ETL):** Lectura e ingesta de logs estructurados en formato CSV.
- **Filtrado y Procesamiento:** Identificación automatizada de anomalías y eventos críticos (`ERROR`, `CRITICAL`).
- **Agrupación y Métricas:** Conteo por servicios afectados para detección rápida de cuellos de botella.
- **Exportación Estructurada:** Generación de un informe final en formato JSON para integración con sistemas de tickets.

## 🛠️ Tecnologías
- Python 3
- Pandas
- JSON & CSV Handling

## 🚀 Ejecución
Instalar dependencias necesarias:
```bash
pip install pandas
Ejecutar el script:
python analyzer.py
