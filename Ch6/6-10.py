import sys

def permArray(A, s):
  if not A: raise RuntimeError("Empty")
  numSeen = 0
  
  for i in xrange(len(s)):
    minIndex = start = next = i
    while start!=s[next]:
      next = s[next]
      if next<minIndex: break
    else:
      next, numSeen = i, numSeen + 1
      while start!=s[next]:
        A[next], A[s[next]] = A[s[next]], A[next]
        next, numSeen = s[next], numSeen + 1
      if numSeen == len(s): break

  
  return A
    
if __name__ == '__main__':
  print "The permutation of A is " + str(permArray(['d', 'f', 'b', 'a', 'g'], [2, 0, 1, 3, 4]))

#Variant 6.9.1 appears to be the same problem
