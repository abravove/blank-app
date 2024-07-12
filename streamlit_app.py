import streamlit as st

def main():
    st.title('Línea de Tiempo')

    # Paso 1
    with st.expander("Paso 1: Descripción del paso 1"):
        st.write("Detalles del paso 1")

    # Paso 2
    with st.expander("Paso 2: Descripción del paso 2"):
        st.write("Detalles del paso 2")

    # Paso 3
    with st.expander("Paso 3: Descripción del paso 3"):
        st.write("Detalles del paso 3")

    # Paso 4
    with st.expander("Paso 4: Descripción del paso 4"):
        st.write("Detalles del paso 4")

    # Paso 5
    with st.expander("Paso 5: Descripción del paso 5"):
        st.write("Detalles del paso 5")

    # Paso 6
    with st.expander("Paso 6: Descripción del paso 6"):
        st.write("Detalles del paso 6")

if __name__ == '__main__':
    main()
