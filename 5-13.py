import sys

def multiply(x, y):
  if min(x, y)<=0: raise ValueError("Oops")
  
  total = 0
  from math import log
  
  def add(x, y): #to be done later (or see solutions in book)
    return x+y
    
  while y:
    total = add(total, x<<int(log(y&~(y-1),2)))
    y = y&(y-1)
  return total
  
if __name__ == '__main__':
  print "The product is " + str(multiply(int(sys.argv[1]), int(sys.argv[2])))
