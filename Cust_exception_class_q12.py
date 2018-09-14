class Error(Exception):
 def __init__(self,val):
  self.msg=val + ', value > 5'
try: 
 value = input ('Enter a number')
 if int(value)>5:
  err=Error(value)
  raise err
except err as w:
 print(w.msg)
 