class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2, weight=1, bidirectional=True):
        if 0<=v1 < self.num_vertices and 0<=v2 < self.num_vertices:
           self.matrix[v1][v2] = weight
           if bidirectional:
             self.matrix[v2][v1] = weight

        else:
           print("Error: Vertex index out of bounds.")

    def remove_edge(self, v1, v2, bidirectional=True):
        if 0<=v1 < self.num_vertices and 0<=v2 < self.num_vertices:
            self.matrix[v1][v2] = 0
            if bidirectional:
                self.matrix[v2][v1] = 0

    def print_matrix(self):
        print("\n-- Adjacency Matrix ---")
        for row in self.matrix:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    graph = GraphMatrix(num_vertices=4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.print_matrix()