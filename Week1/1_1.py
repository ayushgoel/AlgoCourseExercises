def comp1(a, b):
  if a[2] < b[2]:
    return -1
  elif a[2] > b[2]:
    return 1
  else:
    if a[0] < b[0]:
      return -1
    else:
      return 1

def comp2(a, b):
  x = a[0]*b[1]
  y = a[1]*b[0]
  if x < y:
    return -1
  elif x > y:
    return 1
  else:
    if a[0] > b[0]:
      return -1
    else:
      return 1

def getWeightedCompletionTime(vals):
  x = 0
  ret = 0
  for i in vals:
    ret += i[0] * (i[1] + x)
    x += i[1]
    #print x, ret
  return ret
 
#with open('jobs_test.txt') as inFile:
with open('jobs.txt') as inFile:
  inFile.readline()
  vals = [[int(j) for j in i.split()] for i in inFile.read().split('\n') if i != '']
  [i.append(i[0] - i[1]) for i in vals]
  [i.append(float(i[0]) / i[1]) for i in vals]

  aVals = sorted(vals, cmp = comp1, reverse = True)
  #print aVals
  print getWeightedCompletionTime(aVals)

  #nVals = sorted(vals, key = lambda x: x[3], reverse = True)
  nVals = sorted(vals, cmp = comp2, reverse = True)
  #print nVals
  print getWeightedCompletionTime(nVals)
 
