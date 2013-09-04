import sys

def rotate(A): 
  """if not checkDim(A): raise RuntimeError("Bad dim")"""
  
  for i in xrange((len(A) + 1)/2):
    for j in xrange(len(A) - 2*i - 1):
      A[i][i+j], A[i+j][len(A) - i - 1], A[len(A) - i-1][len(A)-i-1-j], A[len(A)-i-1-j][i] = A[len(A)-i-1-j][i], A[i][i+j], A[i+j][len(A) - i - 1], A[len(A) - i-1][len(A)-i-1-j]
    
  return A
      
if __name__ == '__main__':
  A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print str(rotate(A))
    