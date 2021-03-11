# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
import os
import json
# This class represents a directed graph
# using adjacency list representation


class Graph:
    # Constructor
    def __init__(self):
        self.graph = make_graph_from_json('romania.json')

    # # function to add an edge to graph
    # def addEdge(self, u, v):
    #     self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, source, goal):
        # Mark all the vertices as not visited
        visited = []
        path = []
        start = source
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(source)
        # if source not in visited:
        #     visited.append(source)

        while queue:

            if(source not in visited):
                visited.append(source)
            if source == goal:
                print("The Path from {} to {} is".format(start, goal))
                print("-->".join(visited))
                break
            # Dequeue a vertex from
            # queue and print it
            source = queue.pop(0)
            for neighbours in self.graph[source]:
                if neighbours not in visited:
                    queue.append(neighbours)


# Driver code


def make_graph_from_json(json_file):
    file_path = os.path.dirname(os.getcwd()) + \
       "\\" + json_file
    with open(file_path) as f:
        map_data = defaultdict(list, json.load(f))
        return map_data


# Create a graph given in
# the above diagram
g = Graph()

g.BFS('Sibiu', 'Pitesti')

# This code is contributed by Neelam Yadav
