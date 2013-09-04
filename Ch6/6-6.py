import sys

def largestIncSubarray(a): #a is the list
  if not a: raise RuntimeError("Bad input")
  elif len(a) == 1: return [0, 0]
  biggestSeen, trailingIndex = [0, 0], 0 #tuples don't allow item assignment!
  
  for j in xrange(1, len(a)):
    if a[j] > a[biggestSeen[1]] and biggestSeen[1]+1==j: biggestSeen[1]+=1
    if a[j] > a[j-1] and j-trailingIndex>biggestSeen[1] - biggestSeen[0]:
      biggestSeen = [trailingIndex, j]
    if a[j]<a[j-1]: trailingIndex = j  
  return biggestSeen
    
if __name__ == '__main__':
  """Include a list "x y z.." in your argument"""
  print "The edge indices of the largest increasing subarray are " + str(largestIncSubarray([int(i) for i in sys.argv[1:]]))

