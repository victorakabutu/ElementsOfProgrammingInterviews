import sys

def swapBits(x, i, j):
  if min(i,j)<0 or max(i,j)>=64:
    raise RuntimeError("Bad input")
    
  if (x>>j) & 1 == (x>>i)&1: return x
  return x^((1<<i) | (1<<j))
  
if __name__ == '__main__':
  """You should pass for parameters an ordered triple "x i j" where x is the integer and i and j are the bits to swap."""
  print "Swapping bits " + sys.argv[2] + " and " + sys.argv[3] + " of "  + sys.argv[1] + " (" + bin(int(sys.argv[1])) + ") gives " + str(swapBits(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
  
