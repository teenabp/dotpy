import re
email = input ("Enter email address:" )

ma= re.match(r'(.*)@(.*)\.com',email)
print ('Username : 'ma.group(1))
print (ma.group(2))