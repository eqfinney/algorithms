#
# All algorithms related to breadth-first search.
# Author: Emily Quinn Finney
#

from contraction import read_graph

# TODO: add doctests to the code

class BFSearcher:

    def __init__(self, graph):
        self.graph = graph
        self.queue = list()
        self.explored = set()
        self.dist_dict = dict()
        self.connected_comps = list()

    def shortest_path(starting_vertex):
        """
        Implements breadth-first search using a queue.
        starting_vertex: the first vertex on which to search
        """
        current_dist = 0
        self.add_to_queue(starting_vertex, current_dist)
        while len(self.queue) != 0:
            current_vertex = self.queue[0]
            current_dist = self.dist_dict[current_vertex]
            list_of_nodes = self.graph[current_vertex]
            for node in list_of_nodes:
                if node not in self.explored:
                    node_dist = current_dist + 1
                    self.add_to_queue(node, node_dist)
            # delete the current index from the queue
            del self.queue[self.queue.index(current_vertex)]

    def add_to_queue(vertex, dist):
        """
        Adds a vertex to a queue and then marks it explored by adding to a set.
        """
        self.queue.append(vertex)
        self.explored.add(vertex)
        self.dist_dict[vertex] = dist
    
    def find_connected():
        """
        Finds all connected components in a graph.
        """
        for node in self.graph.keys:
            if node not in self.explored:
                self.shortest_path(node)
                newly_seen = self.explored - set.union(*self.connected_comps)
                self.connected_comps.append(newly_seen)

        print(self.connected_comps)
                   

if __name__ == '__main__':
    graph = read_graph('graph2.txt')
    MySearch = BFSearcher(graph)
    MySearch.find_connected()
