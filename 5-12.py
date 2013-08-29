import sys

def getIntersection(A, B): #each argument is a tuple (Rx, Ry, Rw, Rh) as described in the problem. It is expected that Rw, Rh>0
  if A[0]>=B[0]: A, B = B, A

  (R0, R1, Rw, Rh), (S0, S1, Sw, Sh) = A, B

  if S1 + Sh <= R1 or R1+Rh<=S1 or R0 + Rw <= S0: return None #depending on your application, you may want to remove the equality conditions
    
  d = f = e = 0
  c = S0
  
  if S1 <= R1:
    d = R1
  else: d = S1
  if S0 + Sw <= R0 + Rw: e = Sw
  else: e = R0 + Rw - S0
  
  if R1<=S1+Sh and S1<=R1: f = S1+Sh-R1
  elif S1 <= R1 + Rh and R1 + Rh <= S1 + Sh: f = R1 + Rh - S1
  elif S1 <= R1 and R1 + Rh <= S1 + Sh: f = Rh
  else: f = Sh
  return (c, d, e, f)
  
if __name__ == '__main__':  
  A, B = (0, 0, 4, 14), (2, 2, 5, 7)
  print "The intersection is " + str(getIntersection(A, B))
