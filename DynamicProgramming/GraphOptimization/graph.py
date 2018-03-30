# -*- coding:utf-8 -*-

# Create Graph ADT

from DynamicProgramming.GraphOptimization import DFS

class Node(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.get_name + '->' + self.dest.get_name()


class WeightedEdge(object):
    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.src.get_name() + '->(' + str(self.weight) + ')' \
               + self.dest.get_name()


class Digraph(object):

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        else:
            self.edges[src].append(dest)

    def children(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.get_name() + '->' \
                         + dest.get_name + '\n'
        return result[:-1]  # omit final newline


class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_node(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


def search(graph, start, end):
    return DFS.dfs(graph, start, end, [], None)


def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)

    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[0]))
    g.add_edge(Edge(nodes[4], nodes[1]))
    g.add_edge(Edge(nodes[0], nodes[5]))
    sp = search(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', DFS.printPath(sp))


if __name__ == '__main__':
    testSP()



















