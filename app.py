
import streamlit as st
import matplotlib.pyplot as plt

from data import load_reviews
from analysis import analyze_reviews, analyze_single_review

st.set_page_config(
    page_title="ReviewLens",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 ReviewLens")
st.subheader("Análise inteligente de avaliações de clientes")

st.write(
    "Entenda o que seus clientes estão dizendo "
    "através da análise de sentimentos."
)

st.divider()

reviews = load_reviews()
results = analyze_reviews(reviews)

total = len(results)
positive = (results["sentimento"] == "positivo").sum()
negative = (results["sentimento"] == "negativo").sum()
neutral = (results["sentimento"] == "neutro").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de avaliações", total)
col2.metric("😊 Positivas", positive)
col3.metric("😞 Negativas", negative)
col4.metric("😐 Neutras", neutral)

st.divider()

st.subheader("📊 Distribuição de sentimentos")

sentiment_counts = results["sentimento"].value_counts()

fig, ax = plt.subplots()

ax.bar(sentiment_counts.index, sentiment_counts.values)
ax.set_xlabel("Sentimento")
ax.set_ylabel("Quantidade")
ax.set_title("Avaliações por sentimento")

st.pyplot(fig)
plt.close(fig)

st.divider()

st.subheader("📝 Avaliações analisadas")

st.dataframe(
    results,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("🔍 Analise uma avaliação")

comment = st.text_area(
    "Digite um comentário de cliente:",
    placeholder="Ex.: A comida estava deliciosa e a entrega foi rápida!"
)

if st.button("Analisar comentário"):
    if comment.strip():
        sentiment = analyze_single_review(comment)

        if sentiment == "positivo":
            st.success("Sentimento identificado: Positivo 😊")
        elif sentiment == "negativo":
            st.error("Sentimento identificado: Negativo 😞")
        else:
            st.info("Sentimento identificado: Neutro 😐")
    else:
        st.warning("Digite um comentário antes de analisar.")

st.caption(
    "ReviewLens | Projeto educacional de análise de sentimentos com Machine Learning."
)

