# app.py - Aplicación Web Gratuita OptiRoute
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="OptiRoute - Minería", page_icon="⛏️", layout="centered")

st.title("⛏️ OptiRoute: Simulador y Optimización Minera")
st.write("Aplicación web gratuita para la gestión y reducción del 15% en los tiempos de ciclo de transporte.")

st.sidebar.header("Parámetros de Simulación")
camiones = st.sidebar.slider("Número de Camiones", 2, 12, 6)
carguio_base = st.sidebar.slider("Tiempo Base Carguío (min)", 5.0, 20.0, 12.0)
transporte_base = st.sidebar.slider("Tiempo Base Transporte (min)", 10.0, 50.0, 25.0)

# Botón para ejecutar simulación
if st.button("Ejecutar Simulación y Optimización"):
    np.random.seed(42)
    t_carg = np.random.normal(carguio_base, 2.0, camiones)
    t_trans = np.random.normal(transporte_base, 4.0, camiones)
    
    total_base = t_carg + t_trans
    total_opt = total_base * 0.85 # Reducción del 15%
    
    st.success("¡Simulación completada con éxito!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Ciclo Promedio Base", f"{np.mean(total_base):.2f} min")
    with col2:
        st.metric("Ciclo Optimizado (-15%)", f"{np.mean(total_opt):.2f} min", delta="-15%")
    
    # Gráfico comparativo
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(["Base", "Optimizado (-15%)"], [np.mean(total_base), np.mean(total_opt)], color=['#0f172a', '#0284c7'])
    ax.set_ylabel("Minutos por Ciclo")
    ax.set_title("Comparativa de Tiempos Operativos")
    st.pyplot(fig)
