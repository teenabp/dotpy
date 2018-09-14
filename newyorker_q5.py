class American:
 def am_meth():
  print('This is class American')
class NewYorker(American):
 def ny_meth():
  print('This is class Ny')
  
American.am_meth()
NewYorker.ny_meth()