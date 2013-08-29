import sys

#Even though mathematically, something like "---3" is considered an integer, we don't bother with those edge cases here
def stringToInt(s): #s is a string
  if not s:
    raise ValueError("Empty string")
  start=count=0
  m=1
  
  #You could also use the isdigit() method here..
  def isInt(x): #takes strings of length 1
    if ord('0')<=ord(x)<=ord('9'): return True
    return False
    
  if s[0]=='-':
    m=-1
    if len(s)>1: start=1 #depending on whether you're allowed to use isnumeric() above, you might need an else clause here
  
  for i in xrange(start, len(s)):
    if not isInt(s[i]): 
      raise ValueError()
    count+= (ord(s[i]) - ord('0'))*10**(len(s) - (i+1)) #careful of off by one errors
    
  return m*count
    
def intToString(x): #x is an integer
  s = [] #since strings in Python are immutable, we use lists as intermediate storage
  
  if x<0:
    s.append('-')
    x*=-1
  elif x==0: return '0'
 
  count, t = -1, x
  while t:
    count+=1
    t/=10    
    
  while x:
    s.append(chr(x/10**count + ord('0')))
    x -= (x/10**count) * 10**count
    count-=1
    
  return ''.join(s)
  
if __name__ == '__main__':  
  print "Your string as an integer is: " + str(stringToInt(raw_input("Enter a string to convert to int: " )))
  print "Your integer as a string is: " + intToString(int(raw_input("Enter an int to convert to string: " )))
 