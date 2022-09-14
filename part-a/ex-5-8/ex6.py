# min1(1 is number one) max1(number one) not l (L)
# Enter the total number: 4 and give enter then type folloing number one by one 87 90 32 5  
L=[]
N=int(input('Enter the total number: '))
print('Enter the numbers one by one')
for i in range(N):
    x=int(input())
    L.append(x)
min1=min(L)
max1=max(L)
posmin=L.index(min1)
posmax=L.index(max1)
print('The minimum number among the given numbers is:',min1)
print('The position of the minimum number is:',posmin)
print('The maximum number among the given numbers is:',max1)
print('The position of the maximum number is:',posmax)
