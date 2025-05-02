####################################################
###                                              ###
### Trabalhando com grafos utilizando networkx   ###
###                                              ###
####################################################
### Prof. Filipo Mor                             ###
####################################################

import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo vazio
G = nx.Graph()

# Adicionar nós individualmente
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Adicionar múltiplos nós de uma só vez
G.add_nodes_from([5, 6, 7])

# Mostrar os nós atuais
print("Nós:", G.nodes())

# Adicionar arestas (ligações entre nós)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Adicionar várias arestas de uma vez
G.add_edges_from([(3, 4), (4, 5), (5, 6)])

# Mostrar as arestas atuais
print("Arestas:", G.edges())

# Remover um nó
G.remove_node(7)
print("Nós após remover o 7:", G.nodes())

# Remover uma aresta
G.remove_edge(2, 3)
print("Arestas após remover (2,3):", G.edges())

# Criar uma aresta com peso
G.add_edge(1, 5, peso=10)
# Obter o peso
peso = G[1][5]['peso']
print("Peso da aresta (1,5):", peso)

# Atualizar o peso de uma aresta
G[1][5]['peso'] = 15
print("Peso atualizado da aresta (1,5):", G[1][5]['peso'])

# Adicionar um nó com atributos
G.add_node(8, nome='Nó8', cor='vermelho')
print("Nós com atributos:", G.nodes(data=True))

# Adicionar uma aresta com atributos
G.add_edge(8, 2, peso=20, tipo='desejado')
print("Arestas com atributos:", G.edges(data=True))

# Visualizar o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')

# Desenhar os rótulos de peso nas arestas
edge_labels = {(u, v): f"{d['peso']}" for u, v, d in G.edges(data=True) if 'peso' in d}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Grafo usando NetworkX")
plt.show()

# Salvar o grafo em um arquivo GEXF
nx.write_gexf(G, "meu_grafo.gexf")
print("Grafo salvo em 'meu_grafo.gexf'.")

# Carregar o grafo de arquivo GEXF
G_carregado = nx.read_gexf("meu_grafo.gexf")
print("Grafo carregado:", G_carregado.nodes())
