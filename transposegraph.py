# function to add an edge from vertex source to vertex destination
# Time O(1)
# Space O(V)
def addEdge(adj, src, dest):
    adj[src].append(dest)

# print adjacency list
# Time O(V + E)
# Space O(V)
def displayGraph(adj, v):
    for i in range(v):
        print(i, "-->", end="")
        for j in range(len(adj[i])):
            print(adj[i][j], end=" ")
        print()


# get the Transpose of a graph, taking adjacency list of a given graph and that of the Transpose graph
# Time O(V + E)
# Space O(V)
def transposeGraph(adj, transpose, v):
    # traverse the adjacency list of given graph. For each edge(u, v) add and edge (v, u) in the transpose graph's adjancency list
    for i in range(v):
        for j in range(len(adj[i])):
            addEdge(transpose, adj[i][j], i)

if __name__ == "__main__":
    v = 5
    adj = [[] for i in range(v)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 4)
    addEdge(adj, 0, 3)
    addEdge(adj, 2, 0)
    addEdge(adj, 3, 2)
    addEdge(adj, 4, 1)
    addEdge(adj, 4, 3)

    # Finding transpose of graph represented 
    # by adjacency list adj[] 
    transpose = [[]for i in range(v)]
    transposeGraph(adj, transpose, v) 
 
    # displaying adjacency list of 
    # transpose graph i.e. b 
    displayGraph(transpose, v)

    # 