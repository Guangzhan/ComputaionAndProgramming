# *-* coding: utf-8 *-*
from DynamicProgramming.GraphOptimization import ShowPath

def bfs(graph, start, end):
    initPath = [start]
    pathQueue = [initPath]

    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', ShowPath.printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.children(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None