import streamlit as st
import pandas as pd

# Configurar el diseño en dos columnas
columna_izquierda, columna_derecha = st.beta_columns(2)

# En la columna izquierda, crear campos de entrada para la edad de cada persona
with columna_izquierda:
    edad_madre = st.number_input("Edad de la Madre", min_value=0, max_value=150, value=30, step=1)
    edad_padre = st.number_input("Edad del Padre", min_value=0, max_value=150, value=35, step=1)
    edad_hermana = st.number_input("Edad de la Hermana", min_value=0, max_value=150, value=25, step=1)

# En la columna derecha, mostrar los resultados
with columna_derecha:
    # Guardar los datos en un diccionario
    datos = {
        "Persona": ["Madre", "Padre", "Hermana"],
        "Edad": [edad_madre, edad_padre, edad_hermana]
    }

    # Crear un DataFrame de Pandas
    df = pd.DataFrame(datos)

    # Mostrar el DataFrame como una tabla
    st.write("Edad de las personas:")
    st.write(df)
