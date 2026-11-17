import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# Exemplos fictícios usados para treinar o modelo
training_reviews = [
    "comida deliciosa e atendimento excelente",
    "adorei o pedido muito bom",
    "entrega rápida e comida saborosa",
    "experiência maravilhosa recomendo",
    "tudo perfeito gostei muito",
    "comida fria e entrega atrasada",
    "pedido errado e atendimento horrível",
    "péssima experiência não recomendo",
    "comida ruim e embalagem amassada",
    "demorou muito e veio tudo errado",
    "a comida estava razoável",
    "o pedido foi normal",
    "não gostei nem desgostei",
    "a entrega demorou um pouco",
    "experiência mediana nada especial",
]

training_labels = [
    "positivo", "positivo", "positivo", "positivo", "positivo",
    "negativo", "negativo", "negativo", "negativo", "negativo",
    "neutro", "neutro", "neutro", "neutro", "neutro",
]


def create_model():
    """Cria e treina o modelo de classificação."""

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    model.fit(training_reviews, training_labels)

    return model


def analyze_reviews(reviews: pd.DataFrame) -> pd.DataFrame:
    """Classifica o sentimento das avaliações."""

    model = create_model()

    result = reviews.copy()
    result["sentimento"] = model.predict(result["comentario"])

    return result


def analyze_single_review(comment: str) -> str:
    """Classifica o sentimento de um comentário individual."""

    model = create_model()

    prediction = model.predict([comment])

    return prediction[0]
