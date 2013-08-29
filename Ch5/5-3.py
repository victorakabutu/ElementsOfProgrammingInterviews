import sys

def swapBits(x, i, j):
  if min(i,j)<0 or max(i,j)>=64:
    raise RuntimeError("Bad input")
    
  if (x>>j) & 1 == (x>>i)&1: return x
  return x^((1<<i) | (1<<j))

"""Since Python integers can have a theoretically unlimited number of bits, you may be asked to talk about how to
reverse the bit of a Python integer x (whose length in bits is unknown). Assuming x is non-negative, you can try the 
following:

return int(bin(x).lstrip('0b').reverse(), 2)

Note that the interpretation of bit reversal here is DIFFERENT from the one below.
"""

def reverseBits(x): #we assume x is a 64 bit integer
  for i in xrange(32): #watch out for off by one errors here in your test cases!
    x = swapBits(x,i,63-i)
  return x
  
if __name__ == '__main__':
  """You should pass for parameters a list of numbers "x y z.." whose bits are to be reversed."""
  for i in sys.argv[1:]:
    print "Reversing bits in " + i + " (" + bin(int(i)) + ") gives " + str(reverseBits(int(i)))
  
 
