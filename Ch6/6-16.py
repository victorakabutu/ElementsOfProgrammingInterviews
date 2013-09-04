import sys

def flipColors(A, t): #t is the pair (x, y)
  from collections import deque
  
  box, s = deque([]), set([t]) #iterative BFS
  
  while box: #can be easily rewritten to avoid use of s
    x, y = box.pop()
    A[x][y] = not A[x][y]
    if x-1>=0 and A[x-1][y]!=A[x][y] and (x-1, y) not in S:
      box.append((x-1, y))
      s.add((x-1, y))
    if x+1<len(A) and A[x+1][y]!=A[x][y] and (x+1, y) not in S:
      box.append((x+1, y))
      s.add((x+1, y))
    if y-1>=0 and A[x][y-1]!=A[x][y] and (x, y-1) not in S:
      box.append((x, y-1))
      s.add((x, y-1))
    if y+1<len(A) and A[x][y+1]!=A[x][y] and (x, y+1) not in S:
      box.append((x, y+1))
      s.add((x, y+1))
      
if __name__ == '__main__':
  A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  printSpiral(A)
    

"""Variant 6.16.1

Alter flipColors() by enclosing the while loop in a for loop over each square in A. If it is not in s, place the current square in box and run the while loop.
Maintain a global count variable and a tempCount variable for each connected region. Update count if tempCount>count. At the end of the while loop, reset box

Variant 6.16.2
This is a data structure problem. Preliminarily compute and store the connected components of A in sets and store those sets in a max heap (sorted by size).
If t = (a, b) is white, set it to black (else return the top of the heap). For each of its four (NSEW) neighbors, consider those which are black and store their
corresponding connected components in lists. Take the union of these connected components and insert it into the heap. If you do not have a dynamic heap, consider
replacing one of the merged components in the heap with the union and calling heapify(). Depending on what you know about the fragmentation of components in A,
this O(n) procedure may be costly."""