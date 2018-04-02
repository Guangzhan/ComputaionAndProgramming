# -*- coding:utf-8 -*-

# Create Graph ADT

from DynamicProgramming.GraphOptimization import DFS
from DynamicProgramming.GraphOptimization import Node
from DynamicProgramming.GraphOptimization import BFS



class Digraph(object):

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.get_name() + '->' \
                         + dest.get_name + '\n'
        return result[:-1]  # omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addNode(self, edge)
        rev = Node.Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node.Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Node.Edge(nodes[0], nodes[1]))
    g.addEdge(Node.Edge(nodes[1], nodes[2]))
    g.addEdge(Node.Edge(nodes[2], nodes[3]))
    g.addEdge(Node.Edge(nodes[2], nodes[4]))
    g.addEdge(Node.Edge(nodes[3], nodes[4]))
    g.addEdge(Node.Edge(nodes[3], nodes[5]))
    g.addEdge(Node.Edge(nodes[0], nodes[2]))
    g.addEdge(Node.Edge(nodes[1], nodes[0]))
    g.addEdge(Node.Edge(nodes[3], nodes[1]))
    g.addEdge(Node.Edge(nodes[4], nodes[0]))
    sp = DFS.search(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', DFS.printPath(sp))
    sq = BFS.bfs(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', DFS.printPath(sq))


if __name__ == '__main__':
    testSP()




















