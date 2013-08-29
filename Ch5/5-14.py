import sys

def divide(x, y):
  ans = 0
  
  while x>=y:
    j = 0
    while x>=(y << (j+1)):
      j+=1
    ans += 1<<j
    x-= y << j
  return ans
if __name__ == '__main__':
  """Include two integers "x y" in your argument to calculate the quotient x/y (integer division)"""
  print "The quotient is " + str(divide(int(sys.argv[1]), int(sys.argv[2])))
