'''Program to implement the follwing operation on
Dictionary
i. To find the length
ii. To copy
ii. To remove an element from a specified key
iv. To get an element from the given key
v. To view key-value pair as a tuple in list
vi. To get the values as a list
vii. To remove the last itemb
viii. To remove all elements'''


d={1001:'Ramu',1002:'Babu',1003:'Kumar',1004:'Somu',1005:'Sia'}
print('The length of the dictionary is: ', len(d))
print('The copied dictionary is: ',d.copy())
print('The removed element is: ',d.pop(1003))
print('The dictionary d after removing 1003 is: ',d)
print('The element in 1002 key is: ',d.get(1002))
print('The key-value pair as a tuple in a list is: ',d.items())
print('The dictionary values as a list is: ',d.values())
print('The removed last item from dictionary is: ',d.popitem())
d.clear()
print('The dictionary after removing all elements is: ',d)

'''
The output is:
The length of the dictionary is: 5
The copied dictionary is: {1001: Ramu', 1002: "Babu',
1003: 'Kumar', 1004: 'Somu', 1005: 'Sita'}
The removed element is: Kumar
The dictionary d after removing 1003 is: {1001:
Ramu', 1002: 'Babu', 1004: "Somu', 1005: "Sita'}
The element in 1002 key is: Babu
The key-value pair as a tuple in a list is:
dict items([(1001, 'Ramu'), (1002, 'Babu'), (1004,
Somu'), (1005, 'Sita" )})
The dictionary values as a list is: dict_values([°Ramu',
Babu', 'Somu', 'Sita'])
The removed last item from dictionary is: (1005, 'Sita)
The dictionary after removing all elements is: {} '''
