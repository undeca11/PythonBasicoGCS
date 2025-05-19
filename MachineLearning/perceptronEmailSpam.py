####################################################
###      PERCEPTRON detector de e-mail spam      ###
###                                              ###
####################################################
### Prof. Filipo Novo Mor - filipomor.com        ###
### github.com/ProfessorFilipo                   ###
####################################################
import numpy as np

# Função para extrair características simples do e-mail
def extrair_caracteristicas(mensagem):
    features = []
    palavras_chave = ['promoção', 'oferta', 'grátis', 'clique', 'dinheiro']
    mensagem_lower = mensagem.lower()
    for palavra in palavras_chave:
        features.append(1 if palavra in mensagem_lower else 0)
    # Pode-se acrescentar mais características aqui
    return np.array(features)

# Dados de treino: mensagens e rótulos (1=spam, 0=não spam)
treinamento = [
    ("Ganhe dinheiro rápido com esta oferta", 1),
    ("Reunião agendada para amanhã", 0),
    ("Clique aqui para uma surpresa grátis", 1),
    ("Seu boleto está disponível", 0),
    ("Promoção imperdível, aproveite agora", 1),
    ("Vamos conferir o relatório da reunião", 0),
    ("Oferta exclusiva: ganhe prêmios", 1),
    ("Atualização do seu cadastro", 0),
    ("Dinheiro fácil, clique já", 1),
    ("Horario da consulta marcada", 0)
]

# Preparar dados para treinamento
X_train = np.array([extrair_caracteristicas(msg) for msg, label in treinamento])
Y_train = np.array([label for msg, label in treinamento])

# Inicializar pesos e bias
np.random.seed(42)
pesos = np.random.randn(X_train.shape[1])
bias = 0.0
taxa_aprendizado = 0.1
epocas = 10

# Treinando o perceptron
for epoca in range(epocas):
    for x, y in zip(X_train, Y_train):
        linear_output = np.dot(x, pesos) + bias
        y_pred = 1 if linear_output >= 0 else 0
        erro = y - y_pred
        pesos += taxa_aprendizado * erro * x
        bias += taxa_aprendizado * erro
    # Opcional: imprimir peso após cada época
    print(f'Época {epoca+1}: pesos={pesos}, bias={bias:.2f}')

# Testando com mensagens novas
mensagens_testes = [
    "Aproveite a oferta grátis agora mesmo",
    "Reunião importante na próxima semana",
    "Clique aqui para ganhar dinheiro fácil",
    "Lembrete: sua consulta está marcada",
    "Promoção limitada, não perca"
]

print("\nClassificação das mensagens de teste:")
for msg in mensagens_testes:
    x_test = extrair_caracteristicas(msg)
    saida = np.dot(x_test, pesos) + bias
    classe = "Spam" if saida >= 0 else "Não Spam"
    print(f'"{msg}" => {classe}')