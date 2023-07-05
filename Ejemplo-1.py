#En este ejemplo, la clase GrafoMatriz representa un grafo utilizando una matriz de adyacencia.

import networkx as nx
import matplotlib.pyplot as plt

class GrafoMatriz:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]

    def agregar_arista(self, origen, destino):
        if origen >= self.num_vertices or destino >= self.num_vertices:
            raise ValueError("Los vértices están fuera de rango")
        self.matriz[origen][destino] = 1
        self.matriz[destino][origen] = 1

    def imprimir_grafo(self):
        G = nx.Graph()
        for i in range(self.num_vertices):
            G.add_node(i)

        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.matriz[i][j] == 1:
                    G.add_edge(i, j)

        nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
        plt.show()


# Ejemplo de uso

grafo = GrafoMatriz(5)

grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 4)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(1, 4)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 4)

grafo.imprimir_grafo()
