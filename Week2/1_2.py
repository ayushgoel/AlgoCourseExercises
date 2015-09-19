import itertools as it
import pprint as pp
import fractions as fr

numberOfBits = 0

def invert(x):
  if x == '1':
    return '0'
  else:
    return '1'

def invertAt(x, n):
  assert(n >= 0)
  return x[:n] + invert(x[n]) + x[(n+1):]

def combos(x):
  ret = []
  for i in it.permutations(range(numberOfBits), 1):
    ret.append(invertAt(x, i[0]))
  for i in it.permutations(range(numberOfBits), 2):
    d1 = invertAt(x, i[0])
    d2 = invertAt(d1, i[1])
    ret.append(d2)
  return ret

with open("clustering_big.txt") as inFile:
  numberOfBits = int(inFile.readline().split()[1])
  nodes = [] 
  log = {}
  for i in inFile:
    a = ''.join(i.split())
    nodes.append(a)
    log[a] = set([a])
  print nodes

  count = 1
  for i in nodes:
    print "Processing", count, i
    count += 1
    for j in combos(i):
      if log.has_key(j) and log[i] != log[j]:
        log[i] = log[j] = log[i].union(log[j])
  print len(log)
  #pp.pprint(log)
  n = fr.Fraction()
  for i in log.values():
    n += fr.Fraction(1, len(i))
  print n

