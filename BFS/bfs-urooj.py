# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation


class Graph:

    # Constructor
    # Function to print a BFS of graph
    def BFS(self, romaniaMap, source, end):
        # Mark all the vertices as not visited
        visited = []
        # Create a queue for BFS
        queue = []
        answer = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(source)
        visited.append(source)

        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            answer.append(s)

            if(s == end):
                print("the path is:", answer)
                break

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in romaniaMap[s]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)


romaniaMap = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}
g = Graph()

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(romaniaMap, 'Arad', 'Bucharest')
