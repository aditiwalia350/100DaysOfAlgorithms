#create a graph using a dictionary
graph={'A':[['B','S'],[False]],
       'B':[['A'],[False]],
       'S':[['A','C','G'],[False]],
       'C':[['S','D','E','F'],[False]],
       'D':[['C'],[False]],
       'E':[['H','C'],[False]],
       'H':[['G','E'],[False]],
       'F':[['C','G'],[False]],
       'G':[['F','S','H'],[False]]}

def DFS():
    #initialise all vertices to not visited
    for vertex in graph:
        #print(vertex)
        if graph[vertex][1][0]==False:
            DFS_Visit(vertex)

def DFS_Visit(vertex):
    graph[vertex][1][0]=True
    print(vertex)
    for node in graph[vertex][0]:
        if graph[node][1][0]==False:
            DFS_Visit(node)

DFS()





