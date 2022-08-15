a=int(input('Enter the value of a: ')) 
b=int(input('Enter the value of b: ')) 
al=a 
bl=b 
while b!=0:
	t=b
    b=a%b
	a=t
print("The GCD of {} and {} is {}".format(a1,b1,a))