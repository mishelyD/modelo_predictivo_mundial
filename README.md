# PREDICCIONES DEL MUNDIAL 2026 - Machine Learning & Analytics

Este repositorio contiene un proyecto completo de extremo a extremo (End-to-End) para predecir y visualizar los resultados del Mundial de Fútbol 2026. El sistema combina datos históricos, ingeniería de características y un modelo de aprendizaje supervisado que actualiza las probabilidades de cada partido de forma dinámica.

🚀 **[CONSULTA_PREDICCIONES](https://modelopredictivomundial-5aunkspzxqjakmlz6jcoao.streamlit.app/)**

## Arquitectura del proyecto

He organizado el flujo de trabajo en tres fases:

1. **Pipeline ETL y procesamiento de datos:** Limpieza y transformación de datos históricos con Python y Pandas. Se eliminan registros huérfanos y se estandariza el fixture oficial del torneo.
2. **Ingeniería de características (Feature Engineering):** Creamos variables basadas en el rendimiento histórico de cada selección: promedios de gol y rachas de los últimos 5 partidos.
3. **Modelado estadístico:** Entrenamos y validamos un clasificador **Random Forest** que estima las probabilidades de victoria local, empate o victoria visitante para cada encuentro.
4. **Despliegue en la nube:** Construimos una interfaz interactiva con **Streamlit**. El tablero funciona como una herramienta de Business Intelligence (con KPIs y filtros por jornada) y consume las predicciones optimizadas del modelo.

## Estructura del repositorio

* `modelo.ipynb`: Notebook de desarrollo donde hacemos el análisis exploratorio, la limpieza de datos y el entrenamiento del modelo.
* `app.py`: Script principal de la interfaz de usuario. Incluye la lógica de los filtros por fecha y la generación de los KPIs que ves en el tablero.
* `predicciones_mundial.csv`: Archivo de datos puente que guarda las predicciones listas para que la aplicación web las muestre.
* `requirements.txt`: Lista de dependencias para que el proyecto funcione exactamente igual en tu máquina o en la nube.
