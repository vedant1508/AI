INF = 9999999

# Get the number of vertices from the user
V = int(input("Enter the number of vertices: "))

# Create an empty 2D array for the adjacency matrix
G = []
print("Enter the adjacency matrix (Enter 0 for no connection):")

# Prompt the user to input the adjacency matrix
for i in range(V):
    row = list(map(int, input().split()))
    if len(row) != V:
        print("Invalid input. Please enter a square matrix.")
        exit()
    G.append(row)

# Get the starting vertex from the user
start_vertex = int(input("Enter the starting vertex (0 to V-1): "))
if start_vertex < 0 or start_vertex >= V:
    print("Invalid starting vertex.")
    exit()

# Remaining code remains the same
selected = [False] * V
no_edge = 0
selected[start_vertex] = True
print("Edge : Weight\n")

while no_edge < V - 1:
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(f"{x} - {y} : {minimum}")
    selected[y] = True
    no_edge += 1
    
#4
# 0 9 75 0
# 9 0 95 19
# 75 95 0 51
# 0 19 51 0
# 3