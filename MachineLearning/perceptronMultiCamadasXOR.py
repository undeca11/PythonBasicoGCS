#########################################################
### Exemplo de perceptron multicamada - problema XOR  ###
#########################################################
### prof. Filipo Mor - maio de 2025
#########################################################
import numpy as np

# Funções de ativação e derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivada(x):
    return x * (1 - x)

# Dados XOR
inputs = np.array([[0,0],
                   [0,1],
                   [1,0],
                   [1,1]])

# Saídas esperadas
outputs = np.array([[0], [1], [1], [0]])

# Inicializar pesos aleatórios
np.random.seed(42)
peso_input_h1 = np.random.uniform(-1, 1, (2, 2))
peso_h1_saida = np.random.uniform(-1, 1, (2, 1))

# Biases
bias_h1 = np.random.uniform(-1, 1, (1, 2))
bias_saida = np.random.uniform(-1, 1, (1,1))

# Taxa de aprendizado
lr = 0.5
epochs = 10000

for epoch in range(epochs):
    # forward
    # camada escondida
    hidden_input = np.dot(inputs, peso_input_h1) + bias_h1
    hidden_output = sigmoid(hidden_input)

    # camada de saída
    final_input = np.dot(hidden_output, peso_h1_saida) + bias_saida
    y_pred = sigmoid(final_input)

    # erro
    erro = outputs - y_pred
    if epoch % 1000 == 0:
        # Print de monitoramento
        print(f"Epoch {epoch} - erro médio: {np.mean(np.abs(erro))}")

    # backpropagation
    delta_saida = erro * sigmoid_derivada(y_pred)
    delta_hid = delta_saida.dot(peso_h1_saida.T) * sigmoid_derivada(hidden_output)

    # atualização dos pesos
    peso_h1_saida += hidden_output.T.dot(delta_saida) * lr
    peso_input_h1 += inputs.T.dot(delta_hid) * lr

    # atualização dos biases
    bias_saida += np.sum(delta_saida, axis=0, keepdims=True) * lr
    bias_h1 += np.sum(delta_hid, axis=0, keepdims=True) * lr

# Teste final
print("\nResultados após treinamento:")
for x in inputs:
    h_input = np.dot(x, peso_input_h1) + bias_h1
    h_output = sigmoid(h_input)

    final_input = np.dot(h_output, peso_h1_saida) + bias_saida
    y = sigmoid(final_input)
    y_bin = np.round(y[0])  # arredonda para 0 ou 1
    #print(f"Entrada: {x} -> Saída prevista: {int(y_bin)} (probabilidade: {y[0][0]:.2f})")
    print(f"Entrada: {x} -> Saída prevista: {int(y_bin[0])} (probabilidade: {y[0][0]:.2f})")


