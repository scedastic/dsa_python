from collections import defaultdict

# Represents a directed graph using adjacency list representation
class Graph:
    def __init__(self) -> None:
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # Add edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Print a BFS of the graph
    def BFS(self, s):
        """Print a Breadth First Search of the graph

        Args:
            s (node): source node
        """

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Queue for BFS
        queue = []

        # Mark the source node as visited
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s.
            # If an adjacent has not been visited, then mark it visited and enqueue it.
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        print() # Newline to separate


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)
    g.BFS(0)