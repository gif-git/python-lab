#Program to implement basic slice and trim string operations

s='Welcome to Python'
print('The sliced string from index 2 to 8 is: ',s[2:9])
print('The sliced string from index 0 10 5 is: ',s[:6])                          
print('The sliced string from index 5 to last is: ',s[5:])


sl=' Good Morning '                      
print('The string after removing leading and trailing white spaces is:',sl.strip())
print('The string after removing leading white spaces is:',sl.lstrip())
print('The string after removing trailing white spaces is:',sl.rstrip())
