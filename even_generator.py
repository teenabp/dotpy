import sys
n = input("Enter the limit:")

def even(n):
	for i in range (int(n)):
		if (i%2==0):
			yield(i)
			
e=even(n)
list=[]
while True:
	try:
		#print(next(e), end=', ')
		list.append(next(e))
		
	except StopIteration:
		print (list)
		sys.exit()

