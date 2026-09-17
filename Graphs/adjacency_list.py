class GraphList:
    def __init__(self):
        self.adjacency_list = {}
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    def add_edge(self, v1, v2, weight=1, bidirectional=True):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adjacency_list[v1].append((v2))
        if bidirectional:
            self.adjacency_list[v2].append((v1))
    def remove_edge(self, v1, v2, bidirectional=True):
        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            if v2 in self.adjacency_list[v1]:
                self.adjacency_list[v1].remove(v2)
        if bidirectional and v2 in self.adjacency_list and v1 in self.adjacency_list[v2]:
            self.adjacency_list[v2].remove(v1)

    def print_list(self):
        print("\n-- Adjacency List ---")
        for vertex, edges in self.adjacency_list.items():
         print(f"Vertex{vertex} -> Connected to: {", ".join(map(str, edges))}")

if __name__ == "__main__":
        graph = GraphList()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)
        graph.print_list()