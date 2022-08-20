l=[] 
n=int(input("Enter the number of words in the list:"))
print("Enter the words one by one")
for i in range(n):
    w=input()
    l.append(w)
x=l[0]
ll=len(x)
for i in l:
    l2=len(i)
    if l2>ll:
        ll=l2
        x=i
print("The longet word in the list{} is {} ".format(l,x))
