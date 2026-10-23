'''
Tuples -> Tuples are built in data types available in python which helps to create immutable 
sequence of values.
'''

# Create a tuple and print it's type
'''
tup = (1,2,3,4)
print(type(tup))
'''

# Tuple Methods 

# 1. tup.index() -> gives the first occurence of the element present in the tuple.

#WAP to print the first occurence of the elements present in the tuple
'''
tup_occurence = (1,2,1,2,1,3,4,5,6)
print(tup_occurence.index[1])
'''

# 2. tup.count() -> gives the count of element present in a tuple.

tup_count = (12,2,3,4,12,2,3,4,12)
x = tup_count.count(12)
print(x)