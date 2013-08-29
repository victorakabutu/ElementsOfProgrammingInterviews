import sys

def closestWeight(x): #we assume x is a 64 bit integer
  for i in xrange(63): #why is this 63 and not 64?
    if 1 <= (x>>i) & 3 <= 2: return x^(3<<i)
  
  raise RuntimeError("Your input is either 0 or 64")
  
if __name__ == '__main__':
  """You should pass for parameters a number "x"."""
  
  print "The closest number to " + bin(int(sys.argv[1])) + " in this norm is " + bin(closestWeight(int(sys.argv[1])))
  
 
