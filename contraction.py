#
# Random Contraction Implementation
# Author: Emily Quinn Finney
#

from collections import defaultdict
import math
import random
from copy import deepcopy
import ipdb


def read_graph(text_file):
    """
    Takes a text file of numbers in the form:
    First column: vertex
    Subsequent columns: nodes connecting to vertex
    and reads them into a list of lists of the same format.
    """
    graph = defaultdict(list)
    with open(text_file, 'r') as f:
        for line in f:
            row = line.split()
            for value in row[1:]:
                graph[row[0]].append(value)

    return graph


def contract_nodes(graph, node1, node2):
    """
    Given a graph, contracts two nodes node1 and node2, removing self-loops.
    graph: a dictionary containing nodes as keys and connecting nodes as values
    node1: a key of the dictionary, first value to contract
    node2: a key of the dictionary, second value to contract
    """

    if node1 == node2:
        return graph
    
    # we will always contract node1 into node2
    graph[node2].extend(graph[node1])

    # remove node1 from the graph
    del graph[node1]
    # and now we have to replace all instances of node1 with node2
    for key in iter(graph):
        # replace all instances of node1 with node2
        graph[key] = [ node2 if x==node1 else x for x in graph[key] ]

    graph = remove_self_loops(graph)

    return graph


def remove_self_loops(graph):
    """
    Given a graph (in the form of a dictionary), removes self-loops.
    graph: a dictionary containing nodes as keys and connecting nodes as values
    """
    for value in iter(graph):
        while value in graph[value]:
            graph[value].remove(value)

    return graph


def one_contraction(graph):
    """
    Given a graph (in the form of a dictionary), implements the random
    contraction algorithm to find the minimum cut.
    graph: a dictionary containing nodes as keys and connecting nodes as values
    """

    while len(graph) > 2:
        # randomly pick two vertices
        keys = list(graph.keys())
        vertex1 = random.choice(keys)
        vertex2 = random.choice(keys)

        # contract the vertices
        graph = contract_nodes(graph, vertex1, vertex2)

    min_cut = len(graph.popitem()[1])

    return min_cut


def random_contraction(graph_full):
    """
    Given a graph (in the form of a dictionary), implements the random
    contraction algorithm n^2*ln(n) times.
    graph: a dictionary containing nodes as keys and connecting nodes as values
    """
    n = len(graph_full)
    num_trials = int(2* n**2 * math.log(n))
    min_cut = n

    for contraction in range(num_trials):
        print(min_cut)
        min_cut = min(min_cut, one_contraction(deepcopy(graph_full)))

    return min_cut

if __name__ == '__main__':
    graph = read_graph('graph.txt')
    print(random_contraction(graph))
