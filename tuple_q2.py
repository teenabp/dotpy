my_tup=(1,2,3,4,5,6,7,8,9,10)
my_list=my_tup
my_list=[i for i in my_list if i%2==0]
my_tup2=tuple(my_list)
print (my_tup2) 