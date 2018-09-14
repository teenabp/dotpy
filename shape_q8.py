class Shapes:
 x=0
class Square(Shapes):
 def __init__(self, length):
  self.length=length
 def area(self):
  sq_area=self.length*self.length
  print (sq_area)
   
sq=Square(2)
sq.area()
