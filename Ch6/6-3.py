import sys

def capacity(A): #A is the list
  if not A: raise RuntimeError("Bad input")
  bigDiff = minIndex = 0
  
  for j in xrange(1, len(A)):
    if A[j][2] - A[minIndex][2] > bigDiff: bigDiff = A[j][2] - A[minIndex][2] 
    elif A[j][2] < A[minIndex][2]: minIndex = j
  
  return bigDiff
    
if __name__ == '__main__':
  A = [(0,4,2), (1,15, 7), (9,23,-44), (2,45,2), (48, 29, -12)]
  print "The capacity is " + str(capacity(A))

