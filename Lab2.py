# Program Name: Lab2.py 
 # Course: IT1114
 # Student Name: Laydix Roblero
 # Assignment Number: Lab
 # Due Date: 09/05/2025
 # Purpose: What does theprogram do? Help us know what varible to use
 #and use elif and if 
 # List Specific resources used to complete the 
import math 
pizza=int(input("number of pizza:")) 
salad=int(input("number of salad:"))


pizza_order=math.ceil((pizza* 3)/12)

pizza_cost=pizza_order*15.99
salad_cost=salad*7.99
total=pizza_cost+salad_cost

discount=0
if pizza_order>10 and salad>10:
    discount=.15*pizza_cost+.15*salad_cost
elif pizza_order >10: discount=.15*pizza_cost
elif salad_cost>10: discount=.15*salad_cost

delivery_fee=0
if total *.07<20.0:delivery_fee=20.0
else:delivery_fee=total*.07
overall_total=total- discount+ delivery_fee

print("Pizza ordered:",pizza_order)
print("pizza cost:$",pizza_cost)
print("salad cost:$",salad_cost)
print("total:$",total)
print("discount:$",discount)
print("Delivery Fee:$",delivery_fee)
print("total amount due $",overall_total)



