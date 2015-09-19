import sys

bestvalues = 0
items = 0
maxweight = 0

def knapsack(i, j):
#   try:
#     n = bestvalues[i][j]
#   except IndexError:
      weight = items[i][1]
      if weight > j:
        return knapsack(i-1, j)
      else:
        c1 = knapsack(i-1, j)
        c2 = knapsack(i-1, j - weight) + items[0]
        n = max(c1, c2)
        return n

def xx(nItems, lim):
  if nItems == 0:
    return 0
  elif itemSize(items[nItems-1]) > lim:
    return recurse(nItems-1,lim)
  else:
    return max(recurse(nItems-1,lim),
        recurse(nItems-1,lim-itemSize(items[nItems-1])) +
        itemValue(items[nItems-1]))


def pack3(items,sizeLimit):
  P = {}

  def recurse(nItems,lim):
    if lim < 100000 and not P.has_key((nItems,lim)):
      P[nItems, lim] = xx(nItems, lim)
      return P(nItems, lim)
    else:
      return xx(nItems, lim)

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

    bestvalues = [[0] * (100000 + 1)
                  for i in xrange(len(items) + 1)]

    bestvalue = knapsack(len(items), maxweight)

    print('Best possible value: {0}'.format(bestvalue))
