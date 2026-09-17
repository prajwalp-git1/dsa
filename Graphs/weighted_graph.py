class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, weight):
        self.add_node(node1)
        self.add_node(node2)
        self.adjacency_list[node1].append((node2, weight))
        self.adjacency_list[node2].append((node1, weight))
    def display(self):
        for node, neighbors in self.adjacency_list.items():
            print(f"{node} --> {neighbors}")


w_graph = WeightedGraph()
w_graph.add_edge("A", "B", 5)
w_graph.add_edge("A", "C", 3)
w_graph.add_edge("B", "D", 2)
print("Weighted Graph representation:")
w_graph.display()