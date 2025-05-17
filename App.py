import streamlit as st
import requests
from api_lotofacil import capturar_ultimos_resultados

st.set_page_config(page_title="Consulta LotoFácil", layout="centered")

st.title("🔍 Consulta de Resultados - LotoFácil")
st.markdown("Esta interface simples busca os concursos diretamente da API.")

abas = st.tabs(["📋 Resultados", "🔌 Teste de API", "🧪 Teste RAW da API"])

with abas[0]:
    qtd = st.slider("Quantidade de concursos para exibir:", min_value=1, max_value=30, value=10)

    if st.button("📥 Buscar Resultados"):
        resultados = capturar_ultimos_resultados(qtd)
        if not resultados:
            st.error("❌ Não foi possível acessar os dados. Verifique a API.")
        else:
            for concurso, dezenas in resultados:
                st.markdown(f"**Concurso {concurso}:** {' - '.join(f'{d:02}' for d in dezenas)}")

with abas[1]:
    st.subheader("🔌 Teste de Conexão com a API")
    try:
        resp = requests.get("https://loteriascaixa-api.herokuapp.com/api/lotofacil/")
        st.write("✅ Status da Requisição:", resp.status_code)
        st.json(resp.json())
    except Exception as e:
        st.error(f"❌ Erro ao acessar a API: {e}")

with abas[2]:
    st.title("Teste de Conexão com API")
    try:
        resp = requests.get("https://loteriascaixa-api.herokuapp.com/api/lotofacil/")
        st.write("✅ Status da Requisição:", resp.status_code)
        st.markdown("### Conteúdo bruto da resposta da API:")
        st.text(resp.text)  # Aqui mostra o texto cru da resposta
    except Exception as e:
        st.error(f"Erro ao acessar a API: {e}")
