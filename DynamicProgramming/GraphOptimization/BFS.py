# *-* coding: utf-8 *-*

from DynamicProgramming.GraphOptimization import DFS

def BFS(graph, start, end):
    initPath = [start]
    pathQuene = [initPath]

    while len(pathQuene) != 0:
        tmpPath = pathQuene.pop(0)
        print('Current BFS path:', DFS.printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.children(lastNode):
            if nextNode not in tmpPath:
                newPath = newPath + [nextNode]
                pathQuene.append(newPath)
    return None