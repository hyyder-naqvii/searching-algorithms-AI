import os
import json
from collections import defaultdict
from queue import PriorityQueue


# NOTE: This implementation of Best First Search uses the function f(n) = h(h)

class Graph:
    def __init__(self):
        self.graph = make_graph_from_json('romania.json')

    # Function to print a BFS of graph
    def BFS(self, source, goal):
        try:
            heuristics = get_heuristic_value_to_goal(
                'romania_heuristics.json', goal)
        except:
            print("Heuristics not available for", goal)
            return
        OPEN = PriorityQueue()
        start = source
        visited = []
        OPEN.put((heuristics[source], source))

        while OPEN:
            source = OPEN.get()[1]
            if(source not in visited):
                visited.append(source)
            if source == goal:
                print("The Path from {} to {} is".format(start, goal))
                print("-->".join(visited))
                break

            for neighbour in self.graph[source]:
                if neighbour not in visited:
                    OPEN.put((heuristics[neighbour], neighbour))


def get_heuristic_value_to_goal(json_file, goal):
    # If you get a [FileNotFoundException] than uncomment any of the below two lines. The first line works on my PC but may give an exception on your end
    # file_path = os.path.dirname(os.getcwd()) + \
    #     "\\Searching-Algorithms\\" + json_file
    file_path = os.path.dirname(os.getcwd()) + \
        json_file
    with open(file_path) as f:
        map_data = json.load(f)[goal]
        return map_data


def make_graph_from_json(json_file):
    # If you get a [FileNotFoundException] than uncomment any of the below two lines. The first line works on my PC but may give an exception on your end
    # file_path = os.path.dirname(os.getcwd()) + \
    #     "\\Searching-Algorithms\\" + json_file
    file_path = os.path.dirname(os.getcwd()) + \
        json_file
    with open(file_path) as f:
        map_data = defaultdict(list, json.load(f))
        return map_data


g = Graph()

g.BFS('Arad', 'Bucharest')
