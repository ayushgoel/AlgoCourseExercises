from math import log
import random

filename = '2sat6.txt'

def preprocess(clauses):
  var = set()
  for i in clauses:
    for j in i:
      var.add(j)
  removables = set()
  for i in var:
    if -i not in var:
      removables.add(i)
  
  new_clauses = list()
  for i in clauses:
    flag = 1
    for j in i:
      if j in removables:
        flag = 0
        break
    if flag:
      new_clauses.append(i)
  return new_clauses

def papadimAlgo(clauses):
  for tt in xrange(int(log(len(clauses)))):
    var = {}
    for i in clauses:
      for j in i:
        if j<=0:
          j = -j

        if not var.has_key(j):
          var[j] = random.randint(0,1)

    n = len(var)
    for xx in xrange(2*n*n):
      flag = 1
      wrong_clause = None
      for i in clauses:
        n = i[0]
        m = i[1]
        a = b = None
        if n<=0:
          n = -n
          a = notter(var[n])
        else:
          a = var[n]
        if m<=0:
          m = -m
          b = notter(var[m])
        else:
          b = var[m]

        ans = a or b
        #print i, n, m, a, b, ans

        if not ans:
          flag = 0
          s = random.randint(0,1)
          #print "Changing: ", s, var[m], not var[m], notter(var[m])
          if s:
            var[m] = notter(var[m])
          else:
            var[n] = notter(var[n])
          break
      if flag:
        print var, clauses
        return True
  return False

def notter(x):
  if x==0:
    return 1
  else:
    return 0

if __name__ == '__main__':
  clauses = []
  with open(filename) as inFile:
    print inFile.readline()
    for i in inFile:
      x = [int(n) for n in i.strip().split()] 
      clauses.append(x)
  
  length = len(clauses)
  while True:
    clauses = preprocess(clauses)
    if len(clauses) == length:
      break
    length = len(clauses)
    print length
  print length

  x = papadimAlgo(clauses)
  print "Answer: ", x

