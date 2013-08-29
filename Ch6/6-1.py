import sys

def dutchFlag(A, b): #A is the list, b is the index into A
  if b<0 or b>=len(A): raise IndexError("Bad input")
  
  
  i=j=1
  A[b], A[0] = A[0], A[b]
  for k in xrange(1, len(A)):
    if A[k] == A[0]:
      A[k], A[j], j = A[j], A[k], j+1
    elif A[k]<A[0]:
      A[k], A[j] = A[j], A[k]
      A[j], A[i] = A[i], A[j]
      i+=1; j+=1
      
  A[0], A[i-1] = A[i-1], A[0]
  return A
    
if __name__ == '__main__':
  """Include an index i and a list "i x y z.." in your argument"""
  print "The sorted list is " + str(dutchFlag([int(i) for i in sys.argv[2:]], int(sys.argv[1])))

 """Variant 6.1.1
 Use a linear scan to store the three distinct values in a dictionary of size 3 (where each value is assigned to a unique value in {0, 1, 2}. Then instead of using the 
 comparison operators as we have, use the dictionary operator to assign an order to the keys.
 
 Variant 6.1.2
 Expand the dictionary, as above. You'll also need an additional variable to track where the 4th values will go. As a problem solving strategy, you should try to solve either
 the original problem above on your whiteboard or variant 6.1.1 before solving this one as that will give you something concrete to branch off.
 
 Variant 6.1.3
 You don't really need a dictionary here. This should remind you of quick sort. Your comparison should be equality with the first element in the list..