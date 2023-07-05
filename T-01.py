# Encontrar los nodos a una distancia dada:
# Escribe una función que tome un grafo y un nodo de inicio, y encuentre todos los nodos que están
# a una distancia dada (por ejemplo, 2) desde el nodo de inicio. Imprime los nodos encontrados.
import networkx as nx

def encontrar_nodos_a_distancia(grafo, nodo_inicio, distancia):
    distancias = nx.single_source_shortest_path_length(grafo, nodo_inicio)
    nodos_encontrados = [nodo for nodo, distancia_encontrada in distancias.items() if distancia_encontrada == distancia]
    return nodos_encontrados

# Ejemplo de uso
grafo = nx.Graph()
grafo.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
grafo.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')])

nodo_inicio = 'A'
distancia_dada = 2

nodos_en_distancia = encontrar_nodos_a_distancia(grafo, nodo_inicio, distancia_dada)
print("Nodos a distancia", distancia_dada, "desde", nodo_inicio, ":")
print(nodos_en_distancia)