# -*- coding:utf-8 -*-


def printPath(path):
    """
    print shortest path for a graph
    :param path: graph node list
    :return: result
    """
    result = ''
    for i in range(len(path)):
        result += str(i)
        if i != len(path)-1:
            result += '->'
    return result


def dfs(graph, start, end, path, shortest):
     """

     :param graph:
     :param start: graph node
     :param end:  graph node
     :param path: node list
     :param shortest:  shortest path
     :return:
     """
     path += [start]
     if start==end:
         return path
     for node in graph.children(start):
         if node not in path:
             if shortest is None or len(path)<len(shortest):
                 newPath = dfs(graph, node, end, path, shortest)
                 if newPath is not None:
                     shortest = newPath
     return shortest


def search(graph, start, end):
    return dfs(graph, start, end, [], None)















