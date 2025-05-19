import numpy as np

# Dados de entrada (features) e rótulos
X = np.array([[2, 3],
              [1, 1],
              [2, 1],
              [3, 2]])
Y = np.array([1, 0, 0, 1])  # Rótulos (classes)

# Inicialização dos pesos e do bias
np.random.seed(42)
weights = np.random.randn(2)
bias = 0.0

# Taxa de aprendizado
learning_rate = 0.1
n_epochs = 10

for epoch in range(n_epochs):
    for x, y in zip(X, Y):
        # Cálculo da saída do perceptron
        linear_output = np.dot(x, weights) + bias
        y_pred = 1 if linear_output >= 0 else 0

        # Atualização dos pesos
        error = y - y_pred
        weights += learning_rate * error * x
        bias += learning_rate * error

    print(f"Epoch {epoch + 1}: Pesos={weights}, Bias={bias}")

# Testar a classificação final
def predict(x):
    return 1 if (np.dot(x, weights) + bias) >= 0 else 0

# Testar com novos exemplos
test_points = np.array([[3, 3], [1, 0]])
for point in test_points:
    print(f"ponto {point} classificado como {predict(point)}")