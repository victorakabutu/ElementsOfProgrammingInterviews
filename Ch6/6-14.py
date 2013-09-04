import sys

def checkSudoku(A):
  """if not checkDim(A): raise RuntimeError("Bad dim")""" #use to check whether A is 9 x 9!
  
  for row in A:
    bitMask = 0
    for elem in row:
      if not elem: continue
      if any((elem<0, elem>9, (elem>0 and bitMask & (1<<elem)))): return False
      bitMask = bitMask | (1<<elem)
  
  for j in xrange(len(A)): #Notice the repetition. You can tuck this into some kind of function.
    bitMask = 0
    for i in xrange(len(A)):
      if not A[i][j]: continue
      if any((A[i][j]<0, A[i][j]>9, (A[i][j]>0 and bitMask & (1<<A[i][j])))): return False
      bitMask = bitMask | (1<<A[i][j])
  
  for r in xrange(3):
    for c in xrange(3):
      bitMask = 0
      for i in xrange(3):
        for j in xrange(3):
          row, col = 3*r + i, 3*c + j
          if not A[row][col]: continue
          if any((A[row][col]<0, A[row][col]>9, (A[row][col]>0 and bitMask & (1 << A[row][col])))): return False
          bitMask = bitMask | (1<<A[row][col])
  return True

    

