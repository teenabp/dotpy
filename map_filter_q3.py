my_list=[i for i in range(10)]
even_list=list(filter(lambda x:x%2==0, my_list))
sq_even=list(map(lambda x:x**2,even_list))
print (sq_even)