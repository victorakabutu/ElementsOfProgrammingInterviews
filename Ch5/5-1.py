import sys
parity = []

def buildTable(): 
  global parity 
  parity = [pHelper(i) for i in xrange(0xFFFF)]
  
def pHelper(x):
  count = 1
  
  while x:
    count^=1
    x = x&(x-1)
  return count^1
  
def parityCheck(x):
  return parity[x&0xFFFF] ^ parity[(x>>16)&0xFFFF] ^ parity[(x>>32)&0xFFFF] ^ parity[(x>>48)&0xFFFF]
  
if __name__ == '__main__':
  """This is a great interview question for a company like Google because it hints at parallelizing
  common tasks. One follow up to ask yourself, for example, is how you would solve this problem if you
  had multiple "compute nodes" at your disposal. You can also think about how to make buildTable() more
  efficient."""
  buildTable()
  for i in sys.argv[1:]:
    print "Parity of " + i + " is " + str(parityCheck(int(i)))
  
