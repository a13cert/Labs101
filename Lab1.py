# Program Name: Lab1.py
# Course: IT1114/Section XXX
# Student Name: Laydix Roblero
# Assignment Number: Lab1
# Due Date: 8/30/2025
# Purpose: Help us determine the sqft,tx,and total cost with the users input.
# List specific resources used to complete the assignment.
# The python video provided

#length
length= float(input("please enter lengh of room:"))
#width
width= float(input("please enter width of room:"))
#cost
cost= float(input("please enter cost per sqft:"))
#calculating are 
squareFT=length*width
#Calculating cost
costFlooring=squareFT*cost
#Tax
tax=costFlooring*0.07
#calculating tax
total=costFlooring+tax
#print results
print("Square feet:",squareFT)
print("Flooring:",costFlooring)
print("Tax:",tax)
print("Total:",total)
