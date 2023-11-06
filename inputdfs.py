# DFS
def dfs(g, s):
    vis[s] = 1
    print(s)
    for c in g[s]:
        if not vis[c]:
            dfs(g, c)

# BFS
def bfs(g, s):
    q = [s]
    vis = [s]
    while q:
        cur = q.pop(0)
        print(cur)
        for c in g[cur]:
            if c not in vis:
                q.append(c)
                vis.append(c)

# Input graph from the user
g = {}
n = int(input("Enter the number of nodes in the graph: "))
for i in range(n):
    neighbors = list(map(int, input(f"Enter neighbors for node {i}: ").split()))
    g[i] = neighbors

# Input the starting node
start_node = int(input("Enter the starting node: "))

# Initialize the visited array
vis = [0] * n

print("DFS:")
dfs(g, start_node)

print("BFS:")
bfs(g, start_node)
