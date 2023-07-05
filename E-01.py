import networkx as nx
import matplotlib.pyplot as plt

my_graph = nx.Graph()
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3)]
my_graph.add_nodes_from(nodes)
my_graph.add_edges_from(edges)

nx.draw(my_graph, with_labels=True)
plt.show()
