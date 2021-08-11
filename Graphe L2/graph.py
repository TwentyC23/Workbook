# python packages needed
import math
import copy
import subprocess
import sys
from os import path
try:
    import networkx as nx
    import matplotlib.pyplot as plt
    import numpy as np
except:
    # install python packages if not already
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'networkx'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
    import networkx as nx
    import matplotlib.pyplot as plt
    import numpy as np

class GraphTheory:
    def __init__(self, file):
        # init the graph (type depending of the matrix symmetry), if load_data failed return
        self.matrix = self.load_data(file)
        if type(self.matrix) != list:
            return
        else:
            for i in range(len(self.matrix)):
                self.matrix[i][i] = math.inf
            self.nodes = [x for x in range(1, len(self.matrix) + 1)]
            if self.Symmetric(self.matrix):
                self.G = nx.Graph()
                self.isSymetric = True
            else:
                self.G = nx.DiGraph()
                self.isSymetric = False
            self.add_edges()

    def load_data(self, file):
        # load data from matrix distance file with text format supported
        dir = path.dirname(__file__)
        data = list()
        try :
            with open(path.join(dir, file), 'r') as f:
                for index, line in enumerate(f):
                    if index == 3:
                        dimension = int(line[13:])
                        break
                for line in f:
                    if line[0] != '#':
                        if len(line.split()) != dimension:
                            temp_data = list(map(int, line.split())) + list(map(int, next(f).split()))
                            while len(temp_data) != dimension:
                                temp_data = temp_data + list(map(int, next(f).split()))
                            data.append(temp_data)
                        else:
                            data.append(list(map(int, line.split())))
        except:
            data = None

        return data

    def Symmetric(self, matrix):
        # check if matrix is symmetric
        for m in range(len(matrix)):
            for n in range(len(matrix)):
                if matrix[m][n] != matrix[n][m]:
                    return False
            return True

    def add_nodes(self):
        # add nodes to the graph
        self.G.clear()
        self.G.add_nodes_from(self.nodes)

    def add_edges(self):
        # add all edges with their weight from the matrix to the graph
        self.add_nodes()
        self.G.add_edges_from((x, y, {'weight': self.matrix[x - 1][y - 1]}) for x in range(1, len(self.nodes) + 1) for y in range(1, len(self.nodes) + 1))

    def NN(self, starting_node):
        # nearest neighbor algorithm
        if starting_node not in self.nodes:
            return None, None

        self.add_edges()

        path = list()
        current_node = starting_node

        # while loop to add all nodes to the path
        while len(path) < len(self.nodes):
            path.append(current_node)
            # list of nearest neighbors of the current node sorted by their weight
            min_weight_neighbors = sorted(self.G[current_node].items(), key = lambda e: e[1]['weight'])
            for increasing_weighted_node in min_weight_neighbors:
                if not increasing_weighted_node[0] in path:
                    current_node = increasing_weighted_node[0]
                    break

        # finalize the path by adding the first node and list all the seights of the edges formed by 2 following nodes
        path.append(starting_node)
        path_weight = [self.G[path[node]][path[node + 1]]['weight'] for node in range(len(path) - 1)]
        path_length = sum(path_weight)

        return path, path_length

    def NI(self, starting_node):
        # nearest insertion algorithm
        if starting_node not in self.nodes:
            return None, None

        self.add_edges()

        current_node = starting_node

        # add first nearest node of starting node to path
        min_weight_neighbors = sorted(self.G[current_node].items(), key = lambda e: e[1]['weight'])
        current_node = min_weight_neighbors[0][0]
        path = [starting_node, current_node, starting_node]

        # while loop to add all nodes to the path (same as NN method)
        while len(path) < len(self.nodes) + 1:
            # var needed to hold the min value of the weights between all the nearest nodes of the different nodes of the current path
            nearest_node = math.inf
            for node in path[:-1]:
                min_weight_neighbors = sorted(self.G[node].items(), key = lambda e: e[1]['weight'])
                for increasing_weighted_node in min_weight_neighbors:
                    if not increasing_weighted_node[0] in path:
                        nearest_node = min(increasing_weighted_node[1]['weight'], nearest_node)
                        # change current node to be the nearest neighbor if its weight is off a smallest value than the current nearest node
                        if nearest_node == increasing_weighted_node[1]['weight']:
                            current_node = increasing_weighted_node[0]

            # list of all the delta C, insert at the index of the minimum value delta C
            min_weight_path = [self.G[path[node]][current_node]['weight'] + self.G[current_node][path[node + 1]]['weight'] - self.G[path[node]][path[node + 1]]['weight'] for node in range(len(path) - 1)]
            path.insert(min_weight_path.index(min(min_weight_path)) + 1, current_node)

        path_weight = [self.G[path[node]][path[node + 1]]['weight'] for node in range(len(path) - 1)]
        path_length = sum(path_weight)

        return path, path_length

    def Fletcher(self, starting_node):
        # Fletcher algorithm
        if starting_node not in self.nodes:
            return None, None

        # reset the graph with only the nodes
        self.add_nodes()

        # sorted list of all the weights in ascending order
        sorted_list = list(filter(lambda x: x!= math.inf, sorted([x for xs in self.matrix for x in xs])))

        # add all edges in sorted_list with the same order while it's not creating a degree 3 node or a cycle (if not all edges are added yet)
        for m in range(len(sorted_list)):
            for n in range(len(self.matrix)):
                for o in range(len(self.matrix[n])):
                    if self.matrix[n][o] == sorted_list[m] and self.G.degree[n + 1] < 2 and self.G.degree[o + 1] < 2 and (self.isSymetric or (self.G.succ[n + 1] == {} and self.G.pred[o + 1] == {})):
                        self.G.add_edge(n + 1, o + 1, weight = self.matrix[n][o])
                        try:
                            nx.find_cycle(self.G, n + 1)
                            if self.G.number_of_edges() != len(self.nodes):
                                self.G.remove_edge(n + 1, o + 1)
                        except: pass

        # creat the path by looping through the only cycle in the graph
        path = [node[0] for node in nx.find_cycle(self.G, starting_node)]
        path.append(starting_node)

        path_weight = [self.G[path[node]][path[node + 1]]['weight'] for node in range(len(path) - 1)]
        path_length = sum(path_weight)

        self.add_edges()

        return path, path_length

    def Fletcher_Clarke(self, starting_node):
        # Fletcher & Clarke algorithm
        if starting_node not in self.nodes:
            return None, None

        self.add_nodes()

        savings = [[-math.inf for i in range(len(self.matrix))] for i in range(len(self.matrix))]

        # list of savings calculated following the delta C method
        for m in range(len(savings)):
            for n in range(len(savings)):
                if m != starting_node - 1 and n != starting_node - 1 and m != n:
                    savings[m][n] = self.matrix[m][starting_node - 1] + self.matrix[starting_node - 1][n] - self.matrix[m][n]

        sorted_savings = list(filter(lambda x: x!= -math.inf, sorted([x for xs in savings for x in xs], reverse = True)))

        # same as Fletcher algorithm but by looping through the sorted_saving list
        for m in range(len(sorted_savings)):
            for n in range(len(savings)):
                for o in range(len(savings[n])):
                    if savings[n][o] == sorted_savings[m] and self.G.degree[n + 1] < 2 and self.G.degree[o + 1] < 2 and (self.isSymetric or (self.G.succ[n + 1] == {} and self.G.pred[o + 1] == {})):
                        self.G.add_edge(n + 1, o + 1, weight = self.matrix[n][o])
                        try:
                            nx.find_cycle(self.G, n + 1)
                            if self.G.number_of_edges() != len(self.nodes):
                                self.G.remove_edge(n + 1, o + 1)
                        except: pass

        # add the edges of the starting node with the two nodes of degree 1
        for node in self.nodes:
            if self.G.degree[node] == 1  and node != starting_node and (self.isSymetric or self.G.succ[node] == {}):
                self.G.add_edge(node, starting_node, weight = self.matrix[node - 1][starting_node - 1])
            if self.G.degree[node] == 1 and node != starting_node and (self.isSymetric or self.G.pred[node] == {}):
                self.G.add_edge(starting_node, node, weight = self.matrix[starting_node - 1][node - 1])

        path = [nx.find_cycle(self.G, starting_node)[m][0] for m in range(len(nx.find_cycle(self.G, starting_node)))]
        path.append(starting_node)
        path_weight = [self.G[path[node]][path[node + 1]]['weight'] for node in range(len(path) - 1)]
        path_length = sum(path_weight)

        self.add_edges()

        return path, path_length

    def ER(self, path, path_length):
        # extraction - reinsertion local improvement
        if path == None or path_length == None:
            return None, None

        self.add_edges()

        # loop through all indexes to place the node at a new index
        for oldindex in range(len(path) - 1):
            cost = {}
            for newindex in range(len(path) - 1):
                path_cost = copy.deepcopy(path)
                path_cost.pop(len(path_cost) - 1)
                path_cost.insert(newindex, path_cost.pop(oldindex))

                # cost of the current path
                path_cost.append(path_cost[0])
                path_weight = [self.G[path_cost[node]][path_cost[node + 1]]['weight'] for node in range(len(path_cost) - 1)]

                cost[sum(path_weight)] = path_cost

            # if the smallest cost of all the reinsertion is smaller than the current one, use this path
            if min(cost) < path_length:
                path_length = min(cost)
                path = cost[min(cost)]

        return path, path_length

    def OPT(self, path, path_length):
        # 2-OPT local improvement
        if path == None or path_length == None:
            return None, None

        self.add_edges()

        # loop through the path and create a new one
        for m in range(len(path) - 1):
            cost = {}
            for n in range(len(path) - 1):
                path_cost = copy.deepcopy(path)
                if path_cost[m] != path_cost[n] and path_cost[m] != path_cost[n + 1] and path_cost[m + 1] != path_cost[n]:
                    if m < n:
                        path_cost = path_cost[:m + 1] + path_cost[n:m:-1] + path_cost[n + 1:]
                    else:
                        path_cost = path_cost[:n + 1] + path_cost[m:n:-1] + path_cost[m + 1:]

                    path_weight = [self.G[path_cost[node]][path_cost[node + 1]]['weight'] for node in range(len(path_cost) - 1)]
                    cost[sum(path_weight)] = path_cost

            # if the smallest cost of all the new paths is smaller than the current one, use this path
            if min(cost) < path_length:
                path = cost[min(cost)]
                path_length = min(cost)

        return path, path_length

    def plot(self):
        # plot the graph with all edges
        plt.figure().canvas.set_window_title('Graph project')
        nx.draw_circular(self.G, with_labels = True)
        plt.show()

    def plot_solution(self, path, starting_node, title):
        # plot the solution with starting node in red
        self.add_nodes()
        self.G.add_edges_from([(path[x], path[x + 1]) for x in range(len(path) - 1)])
        plt.figure().canvas.set_window_title(title)
        color_map = list()
        for node in self.G:
            if node == starting_node:
                color_map.append('red')
            else: color_map.append('deepskyblue')
        nx.draw_circular(self.G, node_color = color_map, with_labels = True)
