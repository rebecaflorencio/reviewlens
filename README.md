
# 🔎 ReviewLens

Aplicação de análise de sentimentos de avaliações de clientes utilizando Machine Learning.

O ReviewLens classifica comentários em três categorias: positivo, negativo e neutro, permitindo visualizar a distribuição dos sentimentos e analisar avaliações individuais.

## Funcionalidades

- Classificação de sentimentos em três categorias.
- Visualização da quantidade de avaliações por sentimento.
- Gráfico de distribuição dos resultados.
- Tabela com avaliações classificadas.
- Análise individual de comentários.

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- Scikit-learn
- Matplotlib

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/rebecaflorencio/reviewlens.git
```

### 2. Entre na pasta

```bash
cd reviewlens
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python -m streamlit run app.py
```

## Estrutura do projeto

```text
reviewlens/
├── app.py
├── analysis.py
├── data.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Como funciona

O projeto utiliza TF-IDF para transformar os comentários em representações numéricas e Regressão Logística para realizar a classificação dos sentimentos.

Os exemplos utilizados no treinamento são fictícios e foram criados para fins educacionais.

## Limitações

- O modelo utiliza uma quantidade pequena de exemplos fictícios.
- A classificação pode apresentar erros em comentários diferentes dos exemplos de treinamento.
- O projeto é experimental e não foi validado para uso comercial ou em avaliações reais.

## Melhorias futuras

- Utilizar uma base de avaliações reais e rotuladas.
- Ampliar e avaliar o conjunto de treinamento.
- Comparar diferentes algoritmos de classificação.
- Melhorar a capacidade de generalização do modelo.
