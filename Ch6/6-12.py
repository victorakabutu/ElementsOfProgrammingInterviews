import sys

def nextPerm(A):
  if not A: raise RuntimeError("Empty")
  elif len(A) == 1: return []
  
  def bisect(i, v): #Find the right most number in descending list A[i:] greater than v
    start, end = i, len(A)-1
    candidate = -1

    while start <= end:
      mid = (start + end)/2
      if A[mid] <= v: 
        end = mid - 1
      else: 
        candidate = mid
        start = mid+1
    return candidate
  
  def reverse(i):
    for j in xrange(i, (len(A)+i+1)/2):
      A[j], A[len(A)+i-1-j] = A[len(A)+i-1-j], A[j]
      
  for i in xrange(len(A)-1, 0, -1):
    if A[i-1] < A[i]:
      v = bisect(i, A[i-1])
      A[i-1], A[v] = A[v], A[i-1]
      reverse(i)
      return A
  return []

    
if __name__ == '__main__':
  """Include a list   "x y z.." in your argument"""
  print "The successor of A is " + str(nextPerm([int(v) for v in sys.argv[1:]]))

"""Variant 6.12.1

def kthPerm(n, k): #kth permutation from the identity permutation on [1,...,n]
  i = range(1, n+1)
  if k==1: return i
  
  for i in xrange(2, k+1):
   i = nextPerm(i)
   if not i: return i

#Variant 6.12.2   
def prevPerm(A):
  if not A: raise RuntimeError("Empty")
  elif len(A) == 1: return []
  
  def bisect(i, v): #Find the right most number in descending list A[i:] less than v
    start, end = i, len(A)-1
    candidate = -1

    while start <= end:
      mid = (start + end)/2
      if A[mid] >= v: 
        end = mid - 1
      else: 
        candidate = mid
        start = mid+1
    return candidate
  
  def reverse(i):
    for j in xrange(i, (len(A)+i+1)/2):
      A[j], A[len(A)+i-1-j] = A[len(A)+i-1-j], A[j]
      
  for i in xrange(len(A)-1, 0, -1):
    if A[i-1] > A[i]:
      v = bisect(i, A[i-1])
      A[i-1], A[v] = A[v], A[i-1]
      reverse(i)
      return A
  return []