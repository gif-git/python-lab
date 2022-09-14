# Enter the first value 5 and enter the following number 89 2 78 90 67
L=[]
N=int(input("Enter the total number of list elements:"))
print('Enter the elements one by one:')
for i in range(N):
    x=int(input())
    L.append(x)
print('The original list is:',L)
print('The reversed list is:',end='')
L.reverse()
print(L)
