import random as rd
from math import sqrt
from pprint import pprint

points = []
with open('tsp.txt','r') as f:
  f.readline()
  for i in f:
    i = i.strip().split()
    points.append(tuple([float(i[0]), float(i[1])]))

def init_tour(T):
  return [T[0]]

def dist(p1, p2):
  return sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

def length(T):
  l = 0
  prev = T[0]
  for i in xrange(1, len(T)):
    l += dist(T[i], prev)
    prev = T[i]
  l += dist(T[0], prev)
  return l

def probe_and_insert(node, T):
  if len(T) == 1:
    iterator = [0]
  else:
    iterator = xrange(len(T) - 1)
  distances = [(dist(T[i-1], node) + dist(node, T[i]) - dist(T[i-1], T[i])) for i in iterator]
  minimum = distances.index(min(distances))
  T.insert(minimum, node)
  return T

def process(T):
  tour = init_tour(T)
  for i in xrange(1, len(T)):
#    print i, tour
    tour = probe_and_insert(T[i], tour)
  return length(tour)

x = []
for i in xrange(5000):
  rd.shuffle(points)
  x.append(process(points))
pprint(x)
print "Answer is:", min(x)
