##############################################################
### Exemplo de perceptron multicamada - decisao de compra  ###
##############################################################
### Prof. Filipo Mor - maio de 2025                        ###
##############################################################

import numpy as np

# Função de ativação e sua derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivada(x):
    return x * (1 - x)

# Dados de treinamento: cada elemento é (features, label)
exemplos_treinamento = [
    ((1, 1, 0, 1), 1),   # tenho dinheiro, preciso, NÃO afeta saúde, família feliz -> comprar
    ((0, 1, 1, 1), 1),   # não tenho dinheiro, preciso, afeta saúde, família feliz -> comprar
    ((1, 0, 0, 0), 0),   # tenho dinheiro, não preciso, NÃO afeta saúde, família NÃO feliz -> não comprar
    ((0, 0, 1, 0), 0),   # sem dinheiro, não preciso, afeta saúde, família NÃO feliz -> não comprar
    ((1, 1, 1, 1), 1),   # tudo positivo, deve comprar
    ((0, 0, 0, 1), 0),   # sem dinheiro, não preciso, não afeta saúde, família feliz -> não comprar
    ((1, 0, 1, 1), 1),   # dinheiro, não preciso, afeta saúde, família feliz -> comprar
    ((0, 1, 0, 0), 0),   # sem dinheiro, preciso, não afeta saúde, família não feliz -> não comprar
]

# Extraindo features e labels
X = np.array([features for features, label in exemplos_treinamento])
Y = np.array([[label] for features, label in exemplos_treinamento])

# Normalmente, em problemas pequenos, inicializamos pesos aleatoriamente
np.random.seed(1)
pesos_input_oculto = 2 * np.random.rand(4, 5) - 1  # 4 entradas, 5 perceptrons na camada oculta
pesos_oculto_saida = 2 * np.random.rand(5, 1) - 1 # camada oculta -> saída
bias_oculto = np.random.rand(1, 5)
bias_saida = np.random.rand(1, 1)

# Parâmetros
taxa_aprendizagem = 0.1
epocas = 100000

print("Início do treinamento...")

# Treinamento
for i in range(epocas):
    # Forward propagation
    camada_oculta_input = np.dot(X, pesos_input_oculto) + bias_oculto
    camada_oculta_output = sigmoid(camada_oculta_input)

    camada_saida_input = np.dot(camada_oculta_output, pesos_oculto_saida) + bias_saida
    y_pred = sigmoid(camada_saida_input)

    erro = Y - y_pred
    erro_medio = np.mean(np.abs(erro))

    # Backpropagation
    delta_saida = erro * sigmoid_derivada(y_pred)
    delta_oculta = delta_saida.dot(pesos_oculto_saida.T) * sigmoid_derivada(camada_oculta_output)

    # Atualiza pesos e bias da camada de saída
    pesos_oculto_saida += camada_oculta_output.T.dot(delta_saida) * taxa_aprendizagem
    bias_saida += np.sum(delta_saida, axis=0, keepdims=True) * taxa_aprendizagem

    # Atualiza pesos e bias da camada oculta
    pesos_input_oculto += X.T.dot(delta_oculta) * taxa_aprendizagem
    bias_oculto += np.sum(delta_oculta, axis=0, keepdims=True) * taxa_aprendizagem

    # Imprime erro a cada 10 mil epochs
    if i % 10000 == 0:
        print(f'Época {i}, erro médio: {erro_medio:.4f}')

print("Treinamento finalizado.")

# Teste com novas mensagens
novas_mensagens = [
    ("Clique aqui para ganhar um prêmio!", [1, 1, 1, 1]),  # provável comprar
    ("Reunião às 15h na sala 3.", [0, 1, 0, 0]),           # provável não comprar
    ("Oferta exclusiva: 80% de desconto!", [1, 1, 1, 1]), # comprar
    ("Seu amigo enviou uma foto.", [0, 0, 0, 0]),          # não comprar
    ("Aproveite o desconto exclusivo e economize!", [1, 1, 1, 1]),  # deve comprar
    ("Detalhes da reunião estão no email enviado.", [0, 0, 0, 0]),  # não comprar
    ("Ganhe dinheiro fácil sem esforço na internet!", [1, 1, 1, 0]),  # comprar
    ("Seu pagamento foi processado com sucesso.", [0, 0, 0, 0]),  # não comprar
    ("Oferta por tempo limitado, não perca!", [1, 0, 1, 1]),  # comprar
    ("Revisão do contrato foi finalizada.", [0, 0, 0, 0]),  # não comprar
    ("Última chance: descontos imperdíveis!", [1, 1, 1, 0]),  # comprar
    ("Lembrete: sua senha expira em 3 dias.", [0, 0, 0, 0]),  # não comprar
]

print("\nResultados de teste:")
for msg, feat in novas_mensagens:
    feat = np.array(feat)
    # Forward pass
    camada_oculta = sigmoid(np.dot(feat, pesos_input_oculto) + bias_oculto)
    y_pred = sigmoid(np.dot(camada_oculta, pesos_oculto_saida) + bias_saida)
    classe = 'Comprar' if y_pred >= 0.5 else 'Não comprar'
    print(f"Mensagem: '{msg}'")
    print(f"Features: {feat}")
    print(f"Resposta: {classe} (probabilidade: {y_pred[0][0]:.2f})\n")

