####################################################
###      PERCEPTRON CLASSIFICADOR DE FRASES      ###
###                                              ###
####################################################
### Prof. Filipo Novo Mor - filipomor.com        ###
### github.com/ProfessorFilipo                   ###
####################################################
import numpy as np

# Função para extrair características básicas das frases
def extrair_caracteristicas(frase):
    palavras_chave = ['você', 'é', 'quando', 'como', 'por quê', '?']
    frase_lower = frase.lower()
    # Características: presença de palavras-chave
    return np.array([1 if palavra in frase_lower else 0 for palavra in palavras_chave])

# Dados de treino: lista de frases com labels (1=pergunta, 0=afirmação)
treinamento = [
    ("Você gosta de chocolate?", 1),
    ("Eu gosto de sorvete.", 0),
    ("Quando você vai viajar?", 1),
    ("Ela está feliz hoje.", 0),
    ("Como funciona esse método?", 1),
    ("Estamos começando a reunião.", 0),
    ("Por que você não veio ontem?", 1),
    ("O céu está azul.", 0),
    ("Você sabe a resposta?", 1),
    ("Ele gosta de esportes.", 0)
]

# Preparar os dados para o treinamento
X_train = np.array([extrair_caracteristicas(frase) for frase, label in treinamento])
Y_train = np.array([label for frase, label in treinamento])

# Inicializar pesos e bias
np.random.seed(42)
pesos = np.random.randn(X_train.shape[1])
bias = 0.0

# Configurações de treinamento
taxa_aprendizado = 0.1
epocas = 10

# Treinamento do perceptron
for epoca in range(epocas):
    for x, y in zip(X_train, Y_train):
        linear_output = np.dot(x, pesos) + bias
        y_pred = 1 if linear_output >= 0 else 0
        erro = y - y_pred
        pesos += taxa_aprendizado * erro * x
        bias += taxa_aprendizado * erro
    print(f'Época {epoca+1}: pesos={pesos}, bias={bias:.2f}')

# Frases de teste
frases_teste = [
    "Você vai ao supermercado?",
    "Eu estou cansado.",
    "Quando será o próximo feriado?",
    "Ele gosta de música.",
    "Como você está hoje?",
    "A loja fica aberta até as 10.",
]

print("\nClassificação das frases de teste:")
for frase in frases_teste:
    x_teste = extrair_caracteristicas(frase)
    saida = np.dot(x_teste, pesos) + bias
    classe = "Pergunta" if saida >= 0 else "Afirmação"
    print(f'"{frase}" => {classe}')