# *-* coding: utf-8 *-*

def printPath(path):
    """
    print shortest path for a graph
    :param path: graph node list
    :return: result
    """
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path)-1:
            result += '->'
    return result
