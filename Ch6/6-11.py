import sys

def inversePerm(A):
  if not A: raise RuntimeError("Empty")
  numSeen = 0
  
  for i in xrange(len(A)):
    start = next = i
    while start!=A[next]:
      next = A[next]
      if next<start: break
    else:
      t, numSeen = A[i], numSeen + 1; w, j =  A[t], i
      while True:
        A[t], j, t, numSeen = j, t, w, numSeen + 1; w = A[t] #Note that we had to assign A[t] to w separately
        if start == j: break
      if numSeen == len(A): break

  return A
    
if __name__ == '__main__':
  """Include a list   "x y z.." in your argument"""
  print "The inverse of A is " + str(inversePerm([int(v) for v in sys.argv[1:]]))
