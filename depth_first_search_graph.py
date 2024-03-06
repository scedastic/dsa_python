# DFS traversal from a given  graph
from collections import defaultdict
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self):
        # Default dictionary to sore graph. The graph will be a dictionary of lists
        self.graph = defaultdict(list)

    # Add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # Recur for all vertices adjacent to v
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)


    # Do DFS traversal. Uses recursive DFSUtil()
    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function 
        self.DFSUtil(v, visited)
        print()



if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    start_point = 2
    print(f"The following is Depth First Traversal starting from vertex {start_point}")
    g.DFS(start_point)
    start_point = 0
    print(f"The following is Depth First Traversal starting from vertex {start_point}")
    g.DFS(start_point)
    start_point = 1
    print(f"The following is Depth First Traversal starting from vertex {start_point}")
    g.DFS(start_point)




