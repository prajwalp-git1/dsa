class UnweightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def display(self):
        for node, neighbors in self.adjacency_list.items():
            print(f"{node} --> {neighbors}")

graph = UnweightedGraph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
print("Graph representation:")
graph.display()