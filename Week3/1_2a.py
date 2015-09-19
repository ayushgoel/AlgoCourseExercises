import sys

def itemSize(item): return item[1]
def itemValue(item): return item[0]

def xx(nItems, lim):
  if nItems == 0:
    return 0
  elif itemSize(items[nItems-1]) > lim:
    return recurse(nItems-1,lim)
  else:
    return max(recurse(nItems-1,lim),
        recurse(nItems-1,lim-itemSize(items[nItems-1])) +
        itemValue(items[nItems-1]))
        
def recurse(nItems,lim):
  if lim < 15000000:
    if not P.has_key((nItems,lim)):
      print nItems, lim
#     print items, P
      P[nItems, lim] = xx(nItems, lim)
    return P[nItems, lim]
  else:
    return xx(nItems, lim)

P = {}

def pack3(items,sizeLimit):
  return recurse(len(items),sizeLimit)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: knapsack.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    maxweight = int(lines[0].split()[0])
    items = [map(int, line.split()) for line in lines[1:]]
    sys.setrecursionlimit(20000)

#   bestvalue, reconstruction = knapsack(items, maxweight)
    bestvalue = pack3(items, maxweight)

    print('Best possible value: {0}'.format(bestvalue))
#   print('Items:')
#   for value, weight in reconstruction:
#       print('V: {0}, W: {1}'.format(value, weight))
