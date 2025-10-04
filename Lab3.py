# Program Name: Lab1.py (use the name the program is
# Course: IT1114/Section 3
# Student Name: Laydix Roblero
# Assignment Number: Lab3
# Due Date: 9/12/25
# Purpose: What does the program do (in a few
# List specific resources used to complete the

#ask for goals
sales_goals=float(input("sales goals: "))
#sales one
print("Sales person one")
total_sales= 0
num_people=0
while True:
    for number in range(4):
        print("Week",number+1)
        week=float(input("sales number:"))
        total_sales +=week
    num_people+=1
      
#ask if theres another person
    question= input("Want to add another person? (y/n: ")
    if question == "n":
        break
    #managers Bonus
if total_sales > sales_goals:
      manager_bonus=total_sales*.05
else:
    manager_bonus=total_sales*.02
print("Department Monthly Sales and Commission:")
print("number of employees:",num_people)
print("Department sales goal: $",sales_goals)
print("total sales: $",total_sales)
print("Mgr. Bonus: $",manager_bonus)



 
  


 
