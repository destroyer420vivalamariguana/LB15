import networkx as nx
my_graph = nx.Graph()
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3)]
my_graph.add_nodes_from(nodes)
my_graph.add_edges_from(edges)

nodes = my_graph.nodes()
print("Lista de nodos:", nodes)
edges = my_graph.edges()
print("Lista de aristas:", edges)

if my_graph.has_node(3):
    print("El nodo 3 está presente en el grafo.")
else:
    print("El nodo 3 no está presente en el grafo.")

if my_graph.has_edge(4, 5):
    print("La arista entre los nodos 4 y 5 está presente en el grafo.")
else:
    print("La arista entre los nodos 4 y 5 no está presente en el grafo.")


