class Rectangle:
 def __init__(self,length,breadth):
  self.length=length
  self.breadth=breadth
 def area(self):
  rec_area=self.length*self.breadth
  print (rec_area)
  
rec1=Rectangle(1,2)
rec1.area()