class calculations:

 def power(x,y):
  res=1
  for i in range(y):
   res=res*x
  return res
  
 def sq_of_num():
  list1 =[x*x for x in range(30)]
  print (list1)
  
x,y = input ("Enter numbers x y for x to the power of y: ").split() 
x=int(x)
y=int(y)
print (calculations.power(x,y))

calculations.sq_of_num()