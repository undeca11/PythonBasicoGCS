import matplotlib.pyplot as plt

# Função para desenhar uma caixa de texto maior
def draw_box(ax, text, xy, box_style="round,pad=0.6", fc="#AED6F1", ec="#3498DB", lw=1.5):
    bbox = dict(boxstyle=box_style, facecolor=fc, edgecolor=ec, linewidth=lw)
    ax.text(xy[0], xy[1], text, ha='center', va='center', fontsize=16, bbox=bbox)

# Configura a figura
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')

# Coordenadas dos caixas (x, y)
coords = {
    'start': (0.5, 0.9),
    'forward': (0.5, 0.75),
    'error': (0.5, 0.6),
    'gradient': (0.5, 0.45),
    'update': (0.5, 0.3),
    'loop': (0.5, 0.15),
}
# Desenhar caixas com tamanhos maiores
draw_box(ax, "Início com pesos e biases", coords['start'])
draw_box(ax, "Propagação Direta\n(cálculo da saída)", coords['forward'])
draw_box(ax, "Calcular erro\ny_{true} - y_{pred}", coords['error'])
draw_box(ax, "Calcular o Gradiente\n(com derivadas)", coords['gradient'])
draw_box(ax, "Ajustar pesos e biases\n(novo valor)", coords['update'])
draw_box(ax, "Repetir até erro mínimo", coords['loop'])

# Desenhar setas conectando as caixas
for i in range(5):
    start_xy = (coords[list(coords)[i]][0], coords[list(coords)[i]][1] - 0.02)
    end_xy = (coords[list(coords)[i+1]][0], coords[list(coords)[i+1]][1] + 0.02)
    ax.annotate('', xy=end_xy, xytext=start_xy,
                arrowprops=dict(facecolor='black', arrowstyle='->'))

# Ajustar limites da figura
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Mostrar o fluxo
plt.show()

