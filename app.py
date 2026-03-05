import streamlit as st

def inicializar_sesion():
    if 'usuario_logueado' not in st.session_state:
        st.session_state['usuario_logueado'] = False
    if 'usuario_datos' not in st.session_state:
        st.session_state['usuario_datos'] = None
