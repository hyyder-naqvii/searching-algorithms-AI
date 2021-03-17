from collections import defaultdict
import os
import json


class Graph:
    def __init__(self):
        self.graph = make_graph_from_json('romania.json')

    # # function to add an edge to graph
    # def addEdge(self, u, v):
    #     self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, source, goal):
        visited = []
        start = source
        queue = []

        queue.append(source)

        while queue:
            source = queue.pop(0)
            if(source not in visited):
                visited.append(source)
            if source == goal:
                print("The Path from {} to {} is".format(start, goal))
                print("-->".join(visited))
                break

            for neighbours in self.graph[source]:
                if neighbours not in visited:
                    queue.append(neighbours)


def make_graph_from_json(json_file):
    # If you get a [FileNotFoundException] than uncomment any of the below two lines. The first line works on my PC but may give an exception on your end
    # file_path = os.path.dirname(os.getcwd()) + \
    #     "\\Searching-Algorithms\\" + json_file
    file_path = os.path.dirname(os.getcwd()) + \
        "\\" + json_file
    with open(file_path) as f:
        map_data = defaultdict(list, json.load(f))
        return map_data


g = Graph()

g.BFS('Arad', 'Bucharest')
