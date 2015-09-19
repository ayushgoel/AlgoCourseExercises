import itertools as it
import pprint as pp
import fractions as fr

numberofbits = 0
onebitperms = 0
twobitperms = 0

def invert(x):
  if x == '1':
    return '0'
  else:
    return '1'

def invertat(x, n):
  assert(n >= 0)
  return x[:n] + invert(x[n]) + x[(n+1):]

def combos(x):
  ret = []
  for i in onebitperms:
    ret.append(invertat(x, i[0]))
  for i in twobitperms:
    d1 = invertat(x, i[0])
    d2 = invertat(d1, i[1])
    ret.append(d2)
  return ret

data = {}
counter = 0
def add_single_to_data(x):
  global counter
  #print counter
  data[counter] = set([x])
  counter += 1
  return counter - 1
def is_equal_data(n1, n2):
  #print n1, n2
  return data[n1] == data[n2]
def add_to_data(n1, n2):
  global counter
  #print n1, n2, counter
  data[counter] = data[n1].union(data[n2])
  del data[n1]
  del data[n2]
  counter += 1
  return counter - 1


#nodes = []
log = {}
with open("clustering_big.txt") as infile:
  numberofbits = int(infile.readline().split()[1])
  onebitperms = list(it.permutations(range(numberofbits), 1))
  twobitperms = list(it.permutations(range(numberofbits), 2))
# print onebitperms, twobitperms

  for i in infile:
    a = ''.join(i.split())
#   nodes.append(a)
    #log[a] = set([a])
    log[a] = add_single_to_data(a)
    #print log
  #print nodes

count = 1
for i in log.keys():
  print "Processing", count, i
  count += 1
  for j in combos(i):
    if log.has_key(j) and not is_equal_data(log[i], log[j]):#log[i] != log[j]:
      n1 = log[i]
      n2 = log[j]
      s = add_to_data(n1, n2)
      for d in data[s]:
        if log[d] == n1 or log[d] == n2:
          log[d] = s
      #log[i] = log[j] = s;
      #print log
      #log[i] = log[j] = log[i].union(log[j])
#del(nodes)
print len(log)
#print data#, len(data)
print len(data)


#pp.pprint(log)
#n = fr.Fraction()
#for i in log.values():
#  n += fr.Fraction(1, len(i))
#print "answer:", n

#ans = {}
#x=set()
#for i in log.values():
#  #ans[len(i)] = ans.get(len(i), 0) + 1
#  i=list(i)
#  i.sort()
#  x.add(tuple(i))
#val = 0
#for j in ans.iteritems():
#  print float(j[1])/j[0]
#  val += j[1]/j[0]
#print val
#pp.pprint(x)
#print "New answer :", len(x)

