import sys

def GCD(a, b): #a and b are integeres
  if min(a, b)<=0:
    raise ValueError("Bad input")
  
  gcd = 1
  while True:
    if min(a, b) == 0: return gcd*max(a, b)
    elif min(a, b) == 1: return gcd
    elif (a&1 ^ b&1):
      if a&1: b = b>>1
      else: a = a>>1
    elif not (a&1 | b&1): 
      a, b, gcd = a>>1, b>>1, gcd<<1
    elif a>=b: a, b = b, a-b
    else: b = b-a
    
if __name__ == '__main__':  
  """Include a pair of numbers "x y" as part of your input"""
  print "The GCD is " + str(GCD(int(sys.argv[1]), int(sys.argv[2])))
