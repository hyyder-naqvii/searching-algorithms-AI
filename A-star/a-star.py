import os
import json
from collections import defaultdict
from queue import PriorityQueue


class AStar:
    def __init__(self, goal, debug):
        self.graph = make_graph_from_json('romania-costs.json')
        self.goal = goal
        self.debug = debug
        try:
            self.heuristics = get_heuristic_value_to_goal(
                'romania_heuristics.json', self.goal)
        except:
            print("Heuristics not available for", self.goal)
            return

    # # function to add an edge to graph
    # def addEdge(self, u, v):
    #     self.graph[u].append(v)

    # Function to print a A* of graph

    def a_star(self, source):

        # a priority queue containing all the available paths([Path] Object) to expand
        # Priority queue makes it easy to sort paths in ascending order
        OPEN = PriorityQueue()
        # start = source
        visited = []
        # Convert the start node into a [Path] object
        source = Path(source, self.get_f_cost(source, source))
        # Put the start path object into the priority queue[OPEN] based on it's a_star_cost
        OPEN.put((source.a_star_cost, source))

        while len(OPEN.queue) > 0:
            if(self.debug):
                print("Available Paths")
                for path in OPEN.queue:
                    print("PATH: ", path[1].path,
                          "| A-STAR COST: ", path[1].a_star_cost)
            source = OPEN.get()[1]
            if(self.debug):
                print("Choosing path: ", source.path,
                      "with A-Star Cost: ", source.a_star_cost)
            # source.path.split("-")[-1] retrieves the last node inside a path i.e ("Arad-Sibiu-Fagars") will return Fagaras
            current = source.path.split("-")[-1]

            if(current not in visited):
                visited.append(current)
            if current == self.goal:
                print("=======Path Found=======")
                print(source.path)

                break
            for neighbour in self.graph[current]:
                neighbour_path_to_take = source.path + "-" + neighbour
                neighbour_path = Path(
                    neighbour_path_to_take, self.get_f_cost(source.path, neighbour))
                if(neighbour in visited):
                    continue

                if not self.check_path_already_present(
                        neighbour_path.path, OPEN):
                    OPEN.put((neighbour_path.a_star_cost, neighbour_path))

    # Provide a path string already traversed and get the f-cost from it to the goal(neighbour of the last node of path)

    def get_f_cost(self, path_taken, goal):
        g_cost_of_path = 0
        path_nodes = path_taken.split("-")
        # Add the goal node(next node) to the end of the path traversed
        if(goal not in path_nodes):
            path_nodes.append(goal)

        for i in range(len(path_nodes)-1):
            g_cost_of_path += self.graph[path_nodes[i]][path_nodes[i+1]]
        return g_cost_of_path + self.heuristics[goal]

    def check_path_already_present(self, path, open_queue):
        for p in open_queue.queue:
            if p[1].path == path:
                return True
        return False


# Responsible for backtracking the paths
class Path:
    def __init__(self, path, a_star_cost):
        # path is a string containing all the visited nodes of a path eg (Arad-Sibiu...etc)
        self.path = path
        self.a_star_cost = a_star_cost


def get_heuristic_value_to_goal(json_file, goal):
    # If you get a [FileNotFoundException] than uncomment any of the below two lines. The first line works on my PC but may give an exception on your end
    # file_path = os.path.dirname(os.getcwd()) + \
    #     "\\Searching-Algorithms\\" + json_file
    file_path = os.path.dirname(os.getcwd()) + \
        "\\"+json_file
    with open(file_path) as f:
        map_data = json.load(f)[goal]
        return map_data


def make_graph_from_json(json_file):
    # If you get a [FileNotFoundException] than uncomment any of the below two lines. The first line works on my PC but may give an exception on your end
    # file_path = os.path.dirname(os.getcwd()) + \
    #     "\\Searching-Algorithms\\" + json_file
    file_path = os.path.dirname(os.getcwd()) + \
        "\\"+json_file
    with open(file_path) as f:
        map_data = defaultdict(list, json.load(f))
        return map_data


# goal is needed in the constructor in order to get heuristics value of the goal (i.e Bucharest)
# The A* search only works if the heuristics for the provided goal are available
# In a real life scenario the heuristics will be calculated in real time

# If you want to run the code with debug information (Match your dry run output with code output step by step) then uncomment this line
a_star = AStar("Bucharest", True)
# If you want to run the code without debug information then uncomment this line
# a_star = AStar("Bucharest", False)
a_star.a_star('Arad')
