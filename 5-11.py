import sys

def primeSieve(n):
  if n<2: return []
  A = [bool(not(i%2==0 and i>2)) for i in xrange(n+1)]

  for i in xrange(3, n+1, 2):
    if A[i]:
      for j in xrange(i**2, n+1, i):
        A[j] = False
  return [2]+[i for i in xrange(3,n+1,2) if A[i]] 
  
if __name__ == '__main__':  
  """Include a numbers "x" as part of your input"""
  print "The list of primes <= " + sys.argv[1] + " is " + str(primeSieve(int(sys.argv[1])))
