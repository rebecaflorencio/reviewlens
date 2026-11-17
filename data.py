
import pandas as pd


def load_reviews():
    """Carrega avaliações fictícias para testar o ReviewLens."""

    reviews = [
        {"comentario": "A comida chegou quentinha e estava deliciosa!", "nota": 5},
        {"comentario": "Entrega super rápida, adorei o atendimento.", "nota": 5},
        {"comentario": "O pedido veio errado e faltou uma bebida.", "nota": 1},
        {"comentario": "A comida estava fria e demorou muito.", "nota": 1},
        {"comentario": "Muito bom, compraria novamente!", "nota": 5},
        {"comentario": "O entregador foi educado e gentil.", "nota": 4},
        {"comentario": "A embalagem chegou toda amassada.", "nota": 2},
        {"comentario": "O sabor estava razoável, nada especial.", "nota": 3},
        {"comentario": "Péssima experiência, não recomendo.", "nota": 1},
        {"comentario": "Gostei bastante, tudo veio certinho.", "nota": 4},
        {"comentario": "O restaurante esqueceu meu pedido.", "nota": 1},
        {"comentario": "Excelente qualidade e preço justo.", "nota": 5},
        {"comentario": "A entrega demorou, mas a comida estava boa.", "nota": 3},
        {"comentario": "Atendimento horrível e comida fria.", "nota": 1},
        {"comentario": "Muito saboroso e bem embalado!", "nota": 5},
    ]

    return pd.DataFrame(reviews)
