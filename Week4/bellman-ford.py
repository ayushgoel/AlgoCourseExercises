"""
The Bellman-Ford algorithm

Graph API:

    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
    
"""
 
def initialize(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return d, p

def relax(u, v, graph, d, p):
    if d[v] > d[u] + graph[u][v]:
        d[v]  = d[u] + graph[u][v]
        p[v] = u

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    for u in graph:
        for v in graph[u]:
            try:
              assert d[v] <= d[u] + graph[u][v]
            except AssertionError:
              print "Assert failed: ", v, u
              exit()
    return d, p

def test():
    
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {'a': 4},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
        }
    
    d, p = bellman_ford(graph, 'a')

if __name__ == '__main__': 
  test()
  print "Success1!"

  with open("g3.txt") as inFile:
    graph = {}
    x = inFile.readline().strip().split()
    nn = {}
    for i in xrange(1, int(x[0]) + 1):
      nn[str(i)] = 0
    graph['-1'] = nn
    for i in inFile:
      x = i.strip().split()
      try:
        y = graph[x[0]]
        y[x[1]] = int(x[2])
      except KeyError:
        graph[x[0]] = {x[1]:int(x[2])}
    print "File read!"
    d,p = bellman_ford(graph, '-1')

