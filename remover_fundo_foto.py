import streamlit as st
from PIL import Image
from rembg import remove
import io


def remover_fundo(foto, col1, col2):
    img = Image.open(foto)
    output = remove(img)
    col2.title("Foto sem fundo")
    col2.image(output)

    # Salvar a imagem sem fundo em um buffer de bytes
    output_buffer = io.BytesIO()
    output.save(output_buffer, format="PNG")
    output_buffer.seek(0)

    # Adicionar o botão de download abaixo da foto sem fundo
    col2.download_button(
        label="Download Imagem sem fundo",
        data=output_buffer,
        file_name="imagem_sem_fundo.png",
        mime="image/png",
    )


st.set_page_config(page_title="Remover fundo de fotos", page_icon="📷", layout="wide")

st.title("Removendo fundo de fotos")

foto = st.file_uploader("Escolha uma foto", type=["png", "jpg", "jpeg"])

col1, col2 = st.columns(2)

if foto is not None:
    col1.title("Foto Original")
    col1.image(foto)

    if col1.button("Remover fundo"):
        remover_fundo(foto, col1, col2)
