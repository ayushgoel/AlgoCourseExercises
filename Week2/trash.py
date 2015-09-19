import itertools as it

#a=2

def pp():
  print list(a)

if __name__ == '__main__':
  global a
  a=[1]
  print a
  pp()
  a=list(it.permutations(range(12), 1))
  pp()
  print list(a)


