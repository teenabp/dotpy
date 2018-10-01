import re
from functools import reduce
import os

#### Q1

#res = re.finditer(r"(?:\W|^)([0-9]{1,3})(?:\W|$)", "Exercises number 1, 12, 132222, and 345 are important")
res=re.findall(r"(?:\W|^)([0-9]{1,3})(?:\W|$)", "Exercises number 1, 12, 13222, and 345 are important")
# for n in res:
     # print(n.group(0))
print (res)	 

results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13222, and 345 a1234 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))
	 
#### Q2

string1="find url www.google.com and www.yahoo.com from here"
#.group to make it stirng
#res=re.search("w{3}\.[a-z]+\.[a-z]+",string1).group()
#
res=re.findall("w{3}\.[a-z]+\.[a-z]+",string1)
print(res)

#### Q3

list1=re.split('\W+',string1)
print(list1)


largest=reduce(lambda x,y:x if len(x)>len(y) else y,list1)
print(largest)

largest2=max(list1, key=len)
print (largest2)

#### Q4

file_name=input('Enter filename: ')
size=os.path.getsize('C:\\Users\\nid\\Desktop\\dot_pl\\dotpy\\circle_q6.py')
print(size)
size=os.stat('C:\\Users\\nid\\Desktop\\dot_pl\\dotpy\\circle_q6.py').st_size
print(size)