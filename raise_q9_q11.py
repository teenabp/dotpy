try:
 value = input ('Enter a number: ')
 if int(value)>5:
  raise RuntimeError
except RuntimeError as w:
 print('Runtime Error: Value should be < 5')
 
 
