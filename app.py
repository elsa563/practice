import streamlit as st

# Título de la aplicación
st.title("Contador de Palabras")

# Subtítulo
st.subheader("Ingresa un texto y calcula el número de palabras")

# Cuadro de texto para ingresar el texto
input_text = st.text_area("Escribe tu texto aquí:", height=200)

# Botón para contar las palabras
if st.button("Contar palabras"):
    # Validación: si el texto no está vacío
    if input_text.strip():
        # Contar las palabras
        word_count = len(input_text.split())
        st.success(f"El texto contiene **{word_count} palabras**.")
    else:
        st.warning("Por favor, ingresa un texto antes de contar las palabras.")
