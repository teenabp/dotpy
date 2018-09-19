import re
s = input ("\nEnter you address with pincode: ")
ma=re.findall("[a-z]*\d+[a-z]*", s)
print ("\nwords containing  digits are: ")
print (ma)
ma=re.findall(r'(?:\W|^)[0-9]+(?:\W|$)', s)
print ("\nwords composed of  digits only are: ")
print (ma)