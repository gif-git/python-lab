s=input('Enter a string: ')
sl=s
l=len(s)
if l>=3:
    if s[-3:]=='ing':
        s=s+'ly'
    else:
        s=s+'ing'
print('The given string is:',sl)
print('The modified string is:',s)
