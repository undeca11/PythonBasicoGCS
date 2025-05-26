import numpy as np

# Funções de ativação
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivada(x):
    return x * (1 - x)

# Função para extrair features de uma mensagem de texto
'''def extrair_features(mensagem):
    mensagem_lower = mensagem.lower()
    palavras = mensagem.split()
    total_palavras = len(palavras)

    freq_promo = mensagem_lower.count('promoção') / total_palavras if total_palavras > 0 else 0
    tem_link = 1 if ('http://' in mensagem_lower or 'https://' in mensagem_lower or 'www.' in mensagem_lower) else 0
    palavras_maiusculas = sum(1 for p in palavras if p.isupper())
    proporcao_maiusculas = palavras_maiusculas / total_palavras if total_palavras > 0 else 0

    return [freq_promo, tem_link, proporcao_maiusculas] '''

def extrair_features(mensagem):
    mensagem_lower = mensagem.lower()
    palavras = mensagem.split()
    total_palavras = len(palavras)

    # palavras que indicam spam
    palavras_chave = ['promoção', 'dinheiro', 'ganhe', 'desconto', 'facil', 'premio']
    freq_promo = 1 if any(p in mensagem_lower for p in palavras_chave) else 0

    # links
    tem_link = 1 if ('http://' in mensagem_lower or 'https://' in mensagem_lower or 'www.' in mensagem_lower) else 0

    # palavras inteiramente maiúsculas
    palavras_maiusculas = sum(1 for p in palavras if p.isupper())
    proporcao_maiusculas = 1 if palavras_maiusculas > 0 else 0

    return [freq_promo, tem_link, proporcao_maiusculas]


# Novos exemplos de mensagens (texto)
'''mensagens_exemplos = [
    ("Promoção imperdível! Clique aqui.", [0.9, 1, 0.8]),
    ("Reunião agendada para amanhã.", [0.1, 0, 0.2]),
    ("50% OFF em todos os produtos!!!", [0.85, 1, 0.75]),
    ("Seu relatório está pronto para download.", [0.2, 0, 0.3]),
    ("Ganha dinheiro fácil agora mesmo!", [0.8, 1, 0.9]),
    ("Não perca essa oportunidade!", [0.3, 0, 0.2]),
    ("Clique aqui e ganhe dinheiro fácil!", [0.88, 1, 0.85]),
    ("Reunião de equipe às 14h.", [0.0, 0, 0.0]),
    ("Oferta imperdível: 90% OFF!", [0.9, 1, 0.8]),
    ("Seu boleto venceu. Pague agora!", [0.0, 0, 0.0]),
    ("Ganhe dinheiro trabalhando de casa!", [0.85, 1, 0.9]),
    ("Agenda para a próxima semana.", [0.0, 0, 0.0]),
    ("50% de desconto só hoje!", [0.88, 1, 0.86]),
    ("Chamada de vídeo agendada.", [0.0, 0, 0.0])
]'''

mensagens_exemplos = [
    ## Spam
    ("Ganhe dinheiro rápido sem esforço!", [1, 0, 1]),
    ("Clique aqui e economize agora!", [1, 0, 0]),
    ("Oferta imperdível: 80% de desconto!", [1, 0, 1]),
    ("Você foi selecionado para um prêmio!", [1, 0, 0]),
    ("Economize na sua próxima compra!", [1, 0, 0]),
    ("Dinheiro fácil trabalha de casa!", [1, 0, 1]),
    ("Ganho de dinheiro sem trabalho!", [1, 0, 0]),
    ("Promoção exclusiva para você!", [1, 0, 0]),
    ("Clique agora e ganhe premios!", [1, 0, 0]),
    ("Oferta limitada, aproveite!", [1, 0, 0]),
    ("Aproveite esta oportunidade de ganhar dinheiro!", [1, 0, 1]),
    ("Descontos imperdíveis só hoje!", [1, 0, 1]),
    ("Clique aqui e receba seu prêmio!", [1, 0, 1]),
    ("Conquiste sua liberdade financeira!", [1, 0, 1]),
    ("Multiplique seu dinheiro fácil!", [1, 0, 1]),
    ("Sem esforço, lucro garantido!", [1, 0, 1]),
    ## Não spam
    ("Reunião de equipe às 14h.", [0, 0, 0]),
    ("Seu relatório está pronto para download.", [0, 0, 0]),
    ("Atualize seu cadastro na nossa plataforma.", [0, 0, 0]),
    ("Vamos conferir os resultados do trimestre.", [0, 0, 0]),
    ("Pagamento recebido com sucesso.", [0, 0, 0]),
    ("Sua assinatura vai renovar automaticamente.", [0, 0, 0]),
    ("Confirmação do seu agendamento.", [0, 0, 0]),
    ("Chamada de vídeo agendada para amanhã.", [0, 0, 0]),
    ("Seu boleto foi pago com sucesso.", [0, 0, 0]),
    ("Lembrete: sua senha expira em 3 dias.", [0, 0, 0]),
]
# Extraí as features de todos os exemplos
X = np.array([extrair_features(msg) for (msg, _) in mensagens_exemplos])
Y = np.array([[1], [1], [1], [1], [1], [1], [1], [1], [1], [1],
              [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
              [1], [1], [1], [1], [1], [1]])
# Verificar as features
print("Features dos exemplos de treino:")
for i, feat in enumerate(X):
    print(f"Mensagem {i}) '{mensagens_exemplos[i][0]}'")
    print(f"Features: {feat}\n")

# Inicializar pesos e biases
np.random.seed(1)
pesos_input_oculto = 2 * np.random.rand(3, 4) - 1
pesos_oculto_saida = 2 * np.random.rand(4, 1) - 1
bias_oculto = np.random.rand(1, 4)
bias_saida = np.random.rand(1, 1)

# Hiperparâmetros
taxa_aprendizagem = 0.05
epocas = 250000

# Treinamento
for i in range(epocas):
    # Forward
    camada_oculta_input = np.dot(X, pesos_input_oculto) + bias_oculto
    camada_oculta_output = sigmoid(camada_oculta_input)
    camada_saida_input = np.dot(camada_oculta_output, pesos_oculto_saida) + bias_saida
    y_pred = sigmoid(camada_saida_input)
    erro = Y - y_pred
    erro_medio = np.mean(np.abs(erro))

    # Backpropagation
    delta_saida = erro * sigmoid_derivada(y_pred)
    delta_oculta = delta_saida.dot(pesos_oculto_saida.T) * sigmoid_derivada(camada_oculta_output)

    # Atualizar pesos
    pesos_oculto_saida += camada_oculta_output.T.dot(delta_saida) * taxa_aprendizagem
    pesos_input_oculto += X.T.dot(delta_oculta) * taxa_aprendizagem

    # Atualizar biases
    bias_saida += np.sum(delta_saida, axis=0, keepdims=True) * taxa_aprendizagem
    bias_oculto += np.sum(delta_oculta, axis=0, keepdims=True) * taxa_aprendizagem

    # Opcional: exibir o erro de treinamento periodicamente
    if i % 10000 == 0:
        print(f'Época {i}, erro médio: {erro_medio:.4f}')

# Testando com novas mensagens
novas_mensagens = [
    "Clique aqui para ganhar um prêmio!",
    "Reunião às 15h na sala 3.",
    "Oferta exclusiva: 80% de desconto!",
    "Seu amigo enviou uma foto.",
]

print("\nClassificação das novas mensagens:\n")
for msg in novas_mensagens:
    feat = extrair_features(msg)
    # Forward pass
    hidden_layer = sigmoid(np.dot(feat, pesos_input_oculto) + bias_oculto)
    output = sigmoid(np.dot(hidden_layer, pesos_oculto_saida) + bias_saida)
    classe = 'SPAM' if output >= 0.5 else 'NÃO SPAM'
    print(f"Mensagem: '{msg}'")
    print(f"Features: {feat}")
    print(f"Resposta: {classe} (probabilidade: {output[0][0]:.2f})\n")



