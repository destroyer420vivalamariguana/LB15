# Verificar si un grafo es conexo:
# Escribe una función que tome un grafo como entrada y verifique si el grafo es conexo.
# Un grafo es conexo si existe un camino entre cualquier par de nodos.
import networkx as nx

def es_conexo(grafo):
    return nx.is_connected(grafo)

# Ejemplo de uso
grafo = nx.Graph()
grafo.add_nodes_from(['A', 'B', 'C'])
grafo.add_edges_from([('A', 'B')])

conexo = es_conexo(grafo)
if conexo:
    print("El grafo es conexo.")
else:
    print("El grafo no es conexo.")