#
# Depth-first search algorithms
# Author: Emily Quinn Finney
#

from contraction import read_graph
from collections import Counter, defaultdict


class DFSearcher:

    def __init__(self, graph):
        """
        Initializes the depth-first searcher.
        graph: a graph stored in defaultdict data format
        explored: a set of the labels of all nodes explored
        leader: a dictionary that keeps track of which nodes come before which
        node_count: a count of how many nodes have been traversed
        finishing_time: a dict of how many nodes it took to completely finish
        """
        
        self.graph = graph
        self.explored = set()
        self.source = None
        self.leader = Counter()
        self.node_count = 0
        self.finishing_time = {}

    def dfs(self, node, reversed_run):
        """
        Conducts depth-first search on a graph, starting from a given node.
        node: the node from which to start
        """
        # mark s as explored
        self.explored.add(node)
        if not reversed_run:
            self.leader[self.source] += 1
        # for every edge (s, v): if v unexplored, DFS(G, v)
        for edge in self.graph[node]:
            if edge not in self.explored:
                self.dfs(edge, reversed_run)
        if reversed_run:
            self.node_count += 1
            self.finishing_time[self.node_count] = node
                    

    def dfsloop(self, reversed_run):
        """
        Runs a loop that allows for computation of strongly connected components
        """
        # go from greatest to least finishing time
        self.explored = set()
        if not reversed_run:
            n = sorted(list(self.finishing_time.keys()))
        else:
            n = reversed(list(self.graph.keys()))
        for i in n:
            if reversed_run:
                current_node = i
            else:
                current_node = self.finishing_time[i]
            if current_node not in self.explored:
                self.source = current_node
                self.dfs(current_node, reversed_run)


if __name__ == '__main__':
    my_graph = read_graph('scc.txt')
    graph_searcher = DFSearcher(my_graph)
    graph_searcher.dfsloop(True)
    print("finishing time (count, node), is:", graph_searcher.finishing_time)
    graph_searcher.dfsloop(False)
    print("leaderboard (node, source) is:", graph_searcher.leader.most_common(5))
