INF = 999999999
def printSolution(distGraph):
    string = "inf"
    nodes =distGraph.keys()
    for n in nodes:
        print "\t%6s"%(n),
    print " "
    for i in nodes:
        print"%s"%(i),
        for j in nodes:
            if distGraph[i][j] == INF:
                print "%10s"%(string),
            else:
                print "%10s"%(distGraph[i][j]),
        print" "
def floydWarshall(graph):
    nodes = graph.keys()
    distance = {}
    for n in nodes:
        distance[n] = {}
        for k in nodes:
            distance[n][k] = graph[n][k]
    minimumVal = INF
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k]+distance[k][j]
                if minimumVal > distance[i][j]:
                  minimumVal = distance[i][j]
                  print i, j, k, minimumVal
#                print "Check", minimumVal, distance[i][j]
        #printSolution(distance)
#    printSolution(distance)
    print "Answer: ", minimumVal

if __name__ == '__main__':
    graph = {'A':{'A':0,'B':6,'C':INF,'D':6,'E':7},
             'B':{'A':INF,'B':0,'C':5,'D':INF,'E':INF},
             'C':{'A':INF,'B':INF,'C':0,'D':9,'E':3},
             'D':{'A':INF,'B':INF,'C':9,'D':0,'E':7},
             'E':{'A':INF,'B':4,'C':INF,'D':INF,'E':0}
             }
    graph = {'A':{'A':0,'B':-1,'C':-1},
             'B':{'A':-1,'B':0,'C':-1},
             'C':{'A':-1,'B':-1,'C':0},
             }

    with open("g3.txt") as inFile:
      x = inFile.readline().strip().split()
      num_vert = int(x[0]) + 1
      graph = {}
      placeholder = {}
      for i in xrange(1, num_vert):
        placeholder[str(i)] = INF
      for i in xrange(1,num_vert):
        pl = placeholder.copy()
        pl[str(i)] = 0
        graph[str(i)] = pl
      for i in inFile:
        x = i.strip().split()
        graph[x[0]][x[1]] = int(x[2])
    print "File read!"

    floydWarshall(graph)
