class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))

# Get user input for the number of vertices and edges
num_vertices = int(input("Enter the number of vertices: "))
g = Graph(num_vertices)

num_edges = int(input("Enter the number of edges: "))
for i in range(num_edges):
    u, v, w = map(int, input("Enter edge (source destination weight): ").split())
    g.add_edge(u, v, w)

# Call Kruskal's algorithm
g.kruskal_algo()



# Enter the number of vertices: 4
# Enter the number of edges: 5

# Enter edge (source destination weight): 0 1 4
# Enter edge (source destination weight): 0 2 3
# Enter edge (source destination weight): 1 2 2
# Enter edge (source destination weight): 1 3 1
# Enter edge (source destination weight): 2 3 5
