pyg = 'ay'

original = str(input('Enter a word:'))

if len(original) > 0 and original.isalpha():
  word = original.lower()
  
  first = original[0]
  new_word = word[1:len(word)] + first + pyg
  print (original)
  print (new_word)
else:
  print ('empty')
