import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)

G.add_edge(2, 3)
G.add_edge(3, 1)

nodes = [4, 5, 6]
G.add_nodes_from(nodes)

edges = [(4, 5), (5, 6), (6, 4)]
G.add_edges_from(edges)

nx.draw(G, with_labels=True)
plt.show()
