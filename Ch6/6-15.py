import sys

def printSpiral(A):
  """if not checkDim(A): raise RuntimeError("Bad dim")""" #use to check whether A has correct dimensions!
  
  for i in xrange(0, (len(A) + 1)/2):
    if len(A) - 2*i == 1:
      print A[i][i]
      break
    for j in xrange(i, len(A) - i):
      print A[i][j],
    for k in xrange(i+1, len(A) - i):
      print A[k][j],
    for j in xrange(len(A) + i - 2, i-1, -1):
      print A[k][j],
    for k in xrange(len(A) + i - 2, i, -1):
      print A[k][j]

if __name__ == '__main__':
  A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  printSpiral(A)
    

"""Variant 16.5.1, 16.5.2

Initialize the array and use the code in printSpiral(), changing the print statements to assignment statements in a sensible way."""