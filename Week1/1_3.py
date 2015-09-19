def weightOfMST(T):
  return sum([i[2] for i in T])

with open('edges.txt') as inFile:
  x = inFile.readline().split()[0]
  G = [[] for i in xrange(int(x) + 1)]
  print G
  for i in inFile:
    i = [int(j) for j in i.strip().split()]
    G[i[0]].append((i[1], i[2]))
    G[i[1]].append((i[0], i[2]))
  
  # We have the graph now
  # Make a MST

  s = 1
  X = set([s])
  T = [] #MST
  V = set(range(1, int(x) + 1))
  while X != V:
    smll = 9999999999999999
    verN = 0
    verP = 0
    for i in X:
      for j in G[i]:
        if smll > j[1] and j[0] not in X:
          smll = j[1]
          verN = j[0]
          verP = i
    T.append([verP, verN, smll])
    X.add(verN)
  print T
  print weightOfMST(T)


