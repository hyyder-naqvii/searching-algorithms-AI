# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict
import json
import os

# This class represents a directed graph using
# adjacency list representation


class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = make_graph_from_json('romania.json')

    # function to add an edge to graph
    # def addEdge(self, u, v):
    #     self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, source, visited, goal,):

        # Mark the current node as visited
        # and print it
        if source not in visited:
            visited.append(source)
        if(source == goal):
            print("-->".join(visited))

        for neighbour in self.graph[source]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, goal)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, source, goal):
        # Create a set to store visited vertices
        visited = []

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(source, visited, goal)

# Driver code


def make_graph_from_json(json_file):
    file_path = os.path.dirname(os.getcwd()) + \
        "\\"+json_file
    with open(file_path) as f:
        map_data = defaultdict(list, json.load(f))
        return map_data




# # Create a graph given
# # in the above diagram
g = Graph()
print("Following is DFS from (starting from Oradea and Goal is Zerind)")
g.DFS('Oradea', 'Zerind')

# This code is contributed by Neelam Yadav
