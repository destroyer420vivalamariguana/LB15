#Ejemplo de implementación de un grafo utilizando una matriz de adyacencia en Python:

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        if source >= 0 and destination >= 0 and source < self.num_vertices and destination < self.num_vertices:
            self.adj_matrix[source][destination] = 1
            self.adj_matrix[destination][source] = 1

    def remove_edge(self, source, destination):
        if source >= 0 and destination >= 0 and source < self.num_vertices and destination < self.num_vertices:
            self.adj_matrix[source][destination] = 0
            self.adj_matrix[destination][source] = 0

    def print_graph(self):
        for row in self.adj_matrix:
            for val in row:
                print(val, end=" ")
            print()

# Crear un grafo con 5 vértices

graph = Graph(5)

# Agregar conexiones entre los vértices
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# Imprimir el grafo
graph.print_graph()
