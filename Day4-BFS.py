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

root='A'

def BFS(root):
    queue=[]
    queue.append(root)
    #print("queue is",queue)
    graph[root][1]=True

    while(queue):
        element=queue.pop(0)
        #print("popping ",element)
        print(element)
        for i in graph[element][0]:
            if graph[i][1]!=True:
                #print("checking if explored")
                queue.append(i)
                #print("queue is",queue)
                graph[i][1]=True

BFS(root)



