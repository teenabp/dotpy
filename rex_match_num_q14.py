import re
s = input ("\nEnter you address with pincode: ")
ma=re.findall("[a-z]*\d+[a-z]*", s)
print ("\nwords containing  digits are: ")
print (ma)
ma=re.findall("\W\d+\W", s)
print ("\nwords composed of  digits only are: ")
print (ma)