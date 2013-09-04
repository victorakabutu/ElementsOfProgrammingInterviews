import sys

def rotate(i, A):
  if not A or i<0: raise RuntimeError("Error")
  i = i%len(A)
  if i==0: return A
  
  def reverse(start, end): #bread and butter code. Tons of opportunity for index errors!
    for j in xrange(start, (start + end + 1)/2):
      A[j], A[end+start-j] = A[end+start-j], A[j]
      
  reverse(len(A) - i, len(A) - 1)
  reverse(0, len(A) - i - 1)
  A.reverse()
  
  return A

    
if __name__ == '__main__':
  """Include a list   "k x y z.." in your argument where [x y z..] is to be rotated by k positions"""
  print "The rotated list is " + str(rotate(int(sys.argv[1]), [int(v) for v in sys.argv[2:]]))

