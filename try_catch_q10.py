def func(a,b):
 c=a/b
 print(c)
try:
 func(5,0)

except ZeroDivisionError as w:
  print (w)
 