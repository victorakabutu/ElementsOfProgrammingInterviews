import sys

def zeroSum(A): #A is the list
  if not A: raise RuntimeError("Bad input")
  elif len(A) == 1: return {0}
  n = len(A)
  Temp = [A[0] % n] 
  
  for i in xrange(1, len(A)):
    if Temp[-1] == 0: return set(xrange(0, i))
    Temp.append((Temp[i-1] + A[i]) % n)
    
  from collections import Counter
  count = Counter(Temp)
  
  for i in count:
    if count[i]>1:
      a = Temp.index(i)
      b= Temp[a+1:].index(i)+a+1
      return set(range(a, b+1)) #watch out for off by 1 errors!
    
if __name__ == '__main__':
  """Include a list "x y z.." in your argument"""
  print "The zero sum subset is " + str(zeroSum([int(i) for i in sys.argv[1:]]))

