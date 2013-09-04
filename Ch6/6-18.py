import sys

#We use res to get around strings being immutable.
def encodeRLE(s):
  count, index, res = 1, 1, []
  if len(s) ==1: return "1"+s
  
  while index<len(s):
    if s[index]!=s[index-1]:
      res.extend(str(count)+s[index-1])
      count=0
    index+=1; count+=1
  res.extend(str(count)+s[index-1])
  return ''.join(res)
  
def decodeRLE(s):
  index, start, res = 0, 0, []
  
  while start<len(s):
    end = start+1
    while s[end].isdigit():
      end+=1
    res.extend(s[end]*int(s[start:end]))
    start=end+1
  return ''.join(res)
      
if __name__ == '__main__':
  print encodeRLE(sys.argv[1])
  print decodeRLE(sys.argv[2])
    