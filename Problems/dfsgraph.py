def DFS(graph, start, end, path=[]):
    path=path+[start]
    if start==end:
        return path
    for node in graph.childrenOf(start):
                      if not node in path:
                           newpath=DFS(graph, node, end, path)
                           if newpath!=None:
                               return newpath
                           
    return None       