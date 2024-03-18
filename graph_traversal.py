"""Employs both Depth First and Breadth First approaches. Takes code from both `breadth_first_search_graph.py` and `depth_first_search_graph.py`
"""
from collections import defaultdict

class Graph:    
    def __init__(self) -> None:
        # default dictionary to store graph. The graph will be a dictionary of lists
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
    print(f"Following is Breadth First Traversal (starting from vertex {start_point})")
    g.BFS(start_point)
    print(f"The following is Depth First Traversal starting from vertex {start_point}")
    g.DFS(start_point)
    
    start_point = 0
    print(f"Following is Breadth First Traversal (starting from vertex {start_point})")
    g.BFS(start_point)
    print(f"The following is Depth First Traversal starting from vertex {start_point}")
    g.DFS(start_point)