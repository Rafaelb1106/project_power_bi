import streamlit as st
import numpy as np
import pandas as pd
import requests
import smtplib
from PIL import Image
from page_config_dict import PAGE_CONFIG
from page_config_dict import encabezado
st.set_page_config(**PAGE_CONFIG)



encabezado()

def main():
    texto = "Análisis Detallado de la Encuesta Fair's Affairs: Dashboard en Power BI."   
    st.markdown(f'<p style="font-size: 45px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True)
    
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Presento un avanzado dashboard en Power BI, construido a partir de los datos de la encuesta Fairs Affairs. Este recurso proporciona una visualización profunda y detallada de las respuestas, transformando datos cuantitativos en insights claros y accionables.</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Con una interfaz optimizada y herramientas analíticas de vanguardia, los usuarios pueden:</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">- Explorar tendencias emergentes.</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">- Identificar patrones significativos.</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">- Derivar conclusiones basadas en evidencia.</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Esta herramienta es esencial para aquellos que buscan tomar decisiones estratégicas informadas. Invitamos a los interesados a acceder a este recurso para un entendimiento exhaustivo del panorama actual, según lo revelado por la encuesta Fairs Affairs.</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">La información fue sacada de la siguiente base de datos ubicada en esta URL: .</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;"><a href="https://www.kaggle.com/datasets/utkarshx27/fairs-extramarital-affairs-data" target="_blank" style="text-decoration: none;font-size: 17px; color: #000000;">https://www.kaggle.com/datasets/utkarshx27/fairs-extramarital-affairs-data</a></p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([ 12, 2])
    # Contenido de la primera columna
    with col1:
        texto = "En el siguiente botón podemos descargar el fuente del dashboard "   
        st.markdown(f'<p style="font-size: 20px; color: maroon;text-align: right;font-weight: bold;">{texto}</p>', unsafe_allow_html=True)       
   
    with col2:        
        filename = "infidelidad_V1.pbix"
        with open(filename, "rb") as file:
            btn = st.download_button(
            label="Descargar ",
            data=file,
            file_name="infidelidad_V1.pbix",
            mime="application/octet-stream"  
            )
    st.markdown("<hr>", unsafe_allow_html=True)
    ima_dash = Image.open("img/dashboard1.jpg")
    st.image(ima_dash, caption="Resultado final del dashboard ")

    


if __name__ == "__main__":
    main()