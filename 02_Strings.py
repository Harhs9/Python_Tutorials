str1 = "This is a string"
str2 = 'This is also a string with the single quote'
str3 = """This is also a string with the triple quotes.In python, we can create strings 
with these 3 methods."""

# \n -> This is a escape sequence character we use in python if we want to print a sentence in
# another line 

'''
str4 = "My name is Harsh Parihar.\nI am a Aspiring Data Analyst and my goal is to get a job at top-firm."
print(str4)
'''

# String Concatenation 

# It is a process of adding two strings with eachother using the + operator.
'''
a = "My name is Harsh Parihar"
b = "\nI am a Btech Student"

print(a+b) 
'''

# len(str) -> This is a function available in python which helps to give the length of the string.
'''
str1 = "HarshParihar"
print(len(str1))
'''

# Indexing -> Indexing is the process of getting the indexed number of character stored in the string.
'''
str1 = "Harsh Parihar"
ch = str1[4]
print(ch)
'''

# Slicing -> Acessing part of a String is called String Slicing.
"""
str1 = "Harsh Parihar"
str_part= str1[1:6]
print(str_part)
"""

# String Functions 

'''
There are multiple string functions available in python 
'''

# str.endswith() -> This is a function which checks the characters present in the string.
'''
str1 = "My name is Harsh Parihar"
print(str1.endswith("har"))

'''
# str.capitalize() -> This capitalize the first character of the string.
'''
str1 = "my name is harsh parihar"
print(str1.capitalize())
'''

# str.replace() -> This function replaces the characters from old to new.
'''
str1 = "My name is harsh"
print(str1.replace("harsh", "yash"))
'''

# Practice 
# WAP to take the input and of a user name and print it's length
'''
a = str(input("What's your name : "))
print(len(a))
'''

# WAP to find the first occurence of the $ in a string.
'''
str = "My friend is earning $2000"
print(str.find("$")) 
'''

