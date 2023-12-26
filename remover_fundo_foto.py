import streamlit as st
from PIL import Image
from rembg import remove


def remover_fundo(foto, widget):
    img = Image.open(foto)
    output = remove(img)
    widget.title("Foto sem fundo")
    widget.image(output)


st.set_page_config(page_title="Remover fundo de fotos", page_icon="📷", layout="wide")

st.title("Removendo fundo de fotos")

foto = st.file_uploader("Escolha uma foto", type=["png", "jpg", "jpeg"])


col1, col2 = st.columns(2)

if foto is not None:
    col1.title("Foto Original")
    col1.image(foto)
    st.button("Remover fundo", on_click=remover_fundo, args=(foto, col2))
