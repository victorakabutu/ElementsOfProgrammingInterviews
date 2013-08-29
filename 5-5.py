import sys

"""Note that in other languages, 2**(len(S)) will quickly yield to integer overflow.

To test your understanding, you will likely be asked to address this problem. This can
essentially be done without moving away from bit vectors (except that you will now be responsible for
maintaing your own bit vector in a loop of your own design). An example is given below in the solution
to Variant 5.1.1"""

def pSet(S): #S is a list of distinct strings. We assume strings so that the print statements work nicely but you can always typecast
  def printSet(x):
    #The print format leaves a lot to be desired but that's hardly what you're being tested for here
    print "{",
    for i in xrange(len(S)):
      if (x>>i) & 1: print S[i]+",",
    print "}"
  for i in xrange(2**(len(S))):
    printSet(i)
    
  
if __name__ == '__main__':
  """You should pass for parameters a list of numbers  "x y z..."."""
  
  print "The power set is " 
  print pSet(sys.argv[1:])
  
 """Using the machinery here, you can also answer Variant 5.1.1
 The basic idea is to think about how to sort the nCk subsects of S and then print in that sorted order
 
 def printK(k, S): #We assume 0<=k<=len(S) and S is a list of distinct strings
  x, end = 2**k - 1, x << (n-k)
  def printSet(x):
    #The print format leaves a lot to be desired but that's hardly what you're being tested for here
    print "{",
    for i in xrange(len(S)):
      if (x>>i) & 1: print S[i]+",",
    print "}"
  while True:
    printSet(x)
    if x == end: break
    for i in xrange(n-1):
      if (x>>i) & 3 == 1:
        x = x^(3<<i)
        break
"""