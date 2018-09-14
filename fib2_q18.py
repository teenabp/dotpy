n = input("Enter the lenght of the fibonacci series:")
fib = [0,1]
[fib.append(fib[-1] +fib[-2]) for ctr in range(int(n))]
print (fib)