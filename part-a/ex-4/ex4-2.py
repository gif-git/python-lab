def fib(n):
 if n==1:
    return 0
 elif n==2:
    return 1
 else:
    return(fib(n-1)+fib(n-2))
#Main program
n=int(input('Enter the value ofn:'))
if n<=0:
    print('Enter a positive integer')
print('The Fibonacci sequence for {} is:'.format(n))
for i in range(1,n+1):
 print(fib(i),end='')
