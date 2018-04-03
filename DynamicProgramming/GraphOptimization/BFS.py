# *-* coding: utf-8 *-*

from DynamicProgramming.GraphOptimization import ShowPath

def bfs(graph, start, end):
    initPath = [start]
    pathQuene = [initPath]

    while len(pathQuene) != 0:
        tmpPath = pathQuene.pop(0)
        print('Current BFS path:', ShowPath.printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.children(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQuene.append(newPath)
    return None