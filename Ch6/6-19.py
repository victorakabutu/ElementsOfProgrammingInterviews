import sys

#Strings are immutable so this question doesn't really make sense unless you use lists.
#Instead we use this as an opportunity to showcase some other methods
def reverseWords(sentence):
  A = sentence.split()
  A.reverse()
  return ' '.join(A)
  
if __name__ == '__main__':
  print reverseWords(raw_input("Enter sentence: "))
    