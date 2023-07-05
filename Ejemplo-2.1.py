import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo utilizando networkx
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])

# Dibujar el grafo
pos = nx.spring_layout(G)  # Posiciones de los nodos utilizando el algoritmo de Spring layout
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')

# Mostrar el gráfico
plt.title("Grafo")
plt.show()
