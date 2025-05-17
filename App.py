import streamlit as st
from api_lotofacil import capturar_ultimos_resultados

st.set_page_config(page_title="Consulta LotoFácil", layout="centered")

st.title("🔍 Consulta de Resultados - LotoFácil")
st.markdown("Esta interface simples busca os concursos diretamente da API.")

qtd = st.slider("Quantidade de concursos para exibir:", min_value=1, max_value=30, value=10)

if st.button("📥 Buscar Resultados"):
    resultados = capturar_ultimos_resultados(qtd)
    if not resultados:
        st.error("Não foi possível acessar os dados. Verifique a API.")
    else:
        for concurso, dezenas in resultados:
            st.markdown(f"**Concurso {concurso}:** {' - '.join(f'{d:02}' for d in dezenas)}")
