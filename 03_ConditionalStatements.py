# Conditional Statements in python are basically the conditions the user pass based on the result
# he wants to execute for the situation.

"""
There are 3 conditional statements present : 
1 if(condition) :

2 elif(condition) :

3 else(condition) :

"""

# WAP to validate the age of a user for driving license test.
'''
user = int(input("Enter your age : "))

if(user > 18):
    print("You're eligible to give test")

elif(user < 18): 
    print("You're not eligible")
    
'''


# WAP to design the traffic light system where everyone knows the color to react on road
'''
light = input("What is the light color : ")

if(light == "red"):
    print("Please Stop")

elif(light == "Yellow"):
        print("Please Halt")

else:
    print("Go")

'''

# WAP to check the age of the person for voting.
'''
age = int(input("Please Enter Your Age : "))

if(age > 18):
    print("You can vote")

elif(age < 18):
    print("You can't vote")

'''

# WAP for the grading system evaluation based on the marks scored as per subject 

math_marks = int(input("Enter your math's marks : "))
science_marks = int(input("Enter your science marks : "))
english_marks = int(input("Enter your english marks : "))

calc_mark = (math_marks+science_marks+english_marks)/3

print("Your average of marks is : ", calc_mark)

if(calc_mark > 75):
    print("You got a distinction ")

if(calc_mark >= 60 and calc_mark < 75):
    print("You got a division")

elif(calc_mark < 60): 
    print("You need to improve, you did'nt got anything")

