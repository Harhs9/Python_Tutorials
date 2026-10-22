''' 
List -> List in python is a built in data type that stores set of values.
It can store elements of different datatypes.

for ex: [int, float, string, double]

'''

# WAP to store the marks of five students using lists.
'''
marks_students = [98,99,100,91,92]
print(marks_students)
'''

# WAP to print the length and type of the list 
'''
container_veg = ["Dal", "Paneer", "Rajma", "Chai", "Coffee", 12,13]
print(type(container_veg))
print(len(container_veg))
'''

# Write an operation which explain why are Strings immutable and Lists are mutable in python.
'''
str = "hello"
print(str)
str[0] = "y"
'''
'''
student_info = ["Karan", "Delhi", 23, "B.tech"]
print(student_info)
student_info[0] = "Harsh"
print(student_info)

This is how strings are immutable and lists are mutable in python.
'''

# Write an operation to perform list slicing.
'''
student_marks = [89,90,91,92,93,94,95]
print(student_marks[1:5])

slicing [starting index : ending index]
'''

# Write an operation to perform list slicing from 0 to end
'''
student_marks = [89,90,91,92,93,94,95]
print(student_marks[0:])
'''

# Write an operation for list slicing for negative indexes
'''
student_marks = [0,1,2,3,4,5,6,7,8,9]
print(student_marks[-7:-3])
'''

# List Methods: 

# 1. list.append() -> Adds an element to the last.

# WAP to add an element in the list 
'''
marks = [1,2,3,4,5]
marks.append(6)
print(marks)
'''

# 2. list.sort() -> Sorts a list in ascending order
'''
vari = [9,8,7,6,5,4,3,2]
vari.sort()
print(vari)
'''
# 3. list.reverse -> Reverse the list 
'''
revers_list = [1,2,3,4,5]
list.reverse(revers_list)
print(revers_list)
'''

# 4. list.sort(reverse = True) -> Sorts a list in descending order

# WAP to sort a list in descending order
'''
vari = [1,2,3,4,5]
vari.sort(reverse = True)
print(vari)
'''

