#importamos librerias
import pyshorteners #pyshorteners, puedes generar URLs más amigables y compactas
import streamlit as st 
#Streamlit es una biblioteca de Python que facilita la creación de aplicaciones web interactivas
# para la visualización de datos. La notación as st es una convención comúnmente utilizada al importar 
#el módulo streamlit para abreviar el nombre del módulo y hacer que el código sea más conciso.

#se crea un objeto:
def short_url(url):
    s=pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url


#crear una interfaz/streamlit
st.set_page_config(page_title="url shortener",page_icon="📝",layout="centered")
st.image("imagen/www (1).png", use_column_width=True)
st.title("url shortener")
url=st.text_input("ingrese url")
if st.button("url generada"):
    st.write("url shortened: ",short_url(url))

