import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Predicciones - Mundial 2026",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_data
def cargar_datos():
    return pd.read_csv('predicciones_mundial.csv')

df = cargar_datos()


with st.sidebar:
    st.title("FILTROS")
    st.write("Ajusta la jornada para ver las predicciones.")
    
    fechas_disponibles = sorted(df['date'].unique())
    fecha_elegida = st.selectbox("Selecciona una jornada:", fechas_disponibles)
    
    st.divider() # Línea separadora
    
    st.write("**Motor Predictivo:**")
    st.info("Algoritmo: Random Forest\n\nPrecisión de Validación: 54.09%")

st.title("PREDICCIONES DE PARTIDOS - MUNDIAL 2026")
st.markdown("*Sistema de analítica predictiva diseñado para proyectar resultados mediante Machine Learning.*")
st.divider()

partidos_del_dia = df[df['date'] == fecha_elegida]

# --- TARJETAS DE MÉTRICAS (KPIs) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="JORNADA", value=fecha_elegida)
with col2:
    st.metric(label="PARTIDOS PROGRAMADOS", value=len(partidos_del_dia))
with col3:
    st.metric(label="BASE HISTORICA", value=f"{len(df)} partidos")

st.markdown("<br>", unsafe_allow_html=True) 
# --- TABLA ESTILIZADA ---
st.subheader("Cartelera de Pronósticos")

# Configuramos la tabla para que se vea impecable
st.dataframe(
    partidos_del_dia[['home_team', 'away_team', 'prediccion_final']],
    column_config={
        "home_team": "EQUIPO 1",
        "away_team": "EQUIPO 2",
        "prediccion_final": "PRONOSTICO"
    },
    hide_index=True, 
    use_container_width=True 
)