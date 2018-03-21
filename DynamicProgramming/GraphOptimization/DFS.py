# -*- coding:utf-8 -*-

# depth first search


def printPath(path):
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result


def dfs(graph, start, end, path, shortest):
    path = path + [start]
    print('Current DFS path', printPath(path))
    if start == end:
        return path
    for node in graph.children(start):
        if shortest is None or len(path)<len(shortest):
            newPath = dfs(graph, node, end, path, shortest)
            if newPath is not None:
                shortest = newPath
        return shortest
