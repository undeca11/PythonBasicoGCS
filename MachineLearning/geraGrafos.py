import matplotlib.pyplot as plt

# coordenadas dos neurônios
nodes = {
    'x1': (0, 2),
    'x2': (0, 0),
    'h1': (1, 2),
    'h2': (1, 0),
    'saida': (2, 1),
}

# desenhar os neurônios com tamanho maior
for node, (x, y) in nodes.items():
    plt.scatter(x, y, s=400)  # s = tamanho do ponto (quanto maior, maior o diametro)
    plt.text(x, y+0.1, node, ha='center')

# desenhar conexões (setas)
connections = [
    ('x1', 'h1'),
    ('x1', 'h2'),
    ('x2', 'h1'),
    ('x2', 'h2'),
    ('h1', 'saida'),
    ('h2', 'saida'),
]

for start, end in connections:
    x1, y1 = nodes[start]
    x2, y2 = nodes[end]
    plt.arrow(x1 + 0.1, y1, x2 - x1 - 0.2, y2 - y1,
              head_width=0.05, length_includes_head=True)

plt.axis('off')
plt.show()