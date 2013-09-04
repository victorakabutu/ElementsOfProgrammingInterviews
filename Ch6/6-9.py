import sys

def multStrings(s, t):
  if not s or not t: raise RuntimeError("Empty")
  pos = True
  if s[0]=='-':
    pos, s =not pos, s[1:]
    if not s: raise RuntimeError("Empty")
  if t[0]=='-':
    pos, t =not pos, t[1:]
    if not t: raise RuntimeError("Empty")
  
  for k in s:
    if not k.isdigit():
      raise RuntimeError("Non digit")
  for k in t:
    if not k.isdigit():
      raise RuntimeError("Non digit")
  
  #this allows you to write the product back to file (which is what you probably want with BigIntegers)
  #, but I suppose you could use O(1) space (although that defeats the purpose of using BigInts)
  res = [0]*(len(s) + len(t)) 
  if not pos: res.append(0)
  
  def digitMult2(x, y, j):    
    def addNum(j, num):
      while True:
        res[j]+=num
        if res[j]<10: break
        num, res[j], j = res[j]/10, res[j]%10, j-1

    
      
    c = (ord(x) - ord('0')) * (ord(y) - ord('0'))
    addNum(j, c)
    
  def digitMult(x, y, j):
    for i in xrange(len(x)):
      digitMult2(x[-(i+1)], y, j-i)
  
  for j in xrange(len(t)):
    digitMult(s, t[-(j+1)], len(res)-1-j)    

  
  if not pos:
    res[0]='-'
  return ''.join(str(v) for v in res) #ugh. See above note
    
if __name__ == '__main__':
  """Include a pair  "x y" in your argument"""
  print "The product is " + str(multStrings(sys.argv[1], sys.argv[2]))

#Variant 6.9.1 appears to be the same problem
