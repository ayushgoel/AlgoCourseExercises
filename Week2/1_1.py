with open("clustering1.txt") as inFile:
  a=int(inFile.readline())
  clusters = [set([i]) for i in range(1,a+1)]
  #print clusters

  edges = []
  for i in inFile:
    edge = [int(j) for j in i.split()]
    edges.append(edge)

  edges = sorted(edges, key = lambda y: y[2])
  #print edges

  for i in edges:
    n1 = i[0]
    n2 = i[1]
    x = None
    y = None
    for j in clusters:
      if n1 in j:
        x = j
      if n2 in j:
        y = j
    #print "Print : ", i, x, y
    if x!=y:
      if len(clusters) == 4:
        print clusters
        print i
        exit()
      clusters.remove(x)
      clusters.remove(y)
      clusters.append(x.union(y))



