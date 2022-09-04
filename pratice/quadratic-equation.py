# Program to find the roots of a quadratic equation
from math import sqrt
a=float(input('Enter the value of a: '))
b=float(input('Enter the value of b: '))
c=float(input('Enter the value of c: '))
d=b**2-4*a*c
if d>0:
    r1=(-b+sqrt(d))/(2*a)
    r2=(-b-sqrt(d))/(2*a)
    print('There are two roots:',r1,'and',r2)
elif d==0:
    r1=-b/2*a
    print('There is one root:',r1)
else:
    x1=-b/2*a
    x2=sqrt(-d)/2*a
    r1=complex(x1,x2)
    r2=complex(x1,-x2)
    print('The roots are complex ',r1,'and',r2)