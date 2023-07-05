# Encontrar el camino más corto:
# Escribe una función que tome un grafo y dos nodos como entrada, y encuentre el camino más corto
# entre los dos nodos utilizando el algoritmo de Dijkstra. Imprime el camino más corto encontrado.
import networkx as nx

def encontrar_camino_mas_corto(grafo, nodo_inicio, nodo_destino):
    camino_mas_corto = nx.shortest_path(grafo, nodo_inicio, nodo_destino)
    return camino_mas_corto

# Ejemplo de uso
grafo = nx.Graph()
grafo.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
grafo.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('A', 'D')])

nodo_inicio = 'A'
nodo_destino = 'E'

camino_mas_corto = encontrar_camino_mas_corto(grafo, nodo_inicio, nodo_destino)
print("Camino más corto entre", nodo_inicio, "y", nodo_destino, ":")
print(camino_mas_corto)