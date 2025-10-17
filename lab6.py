# Program Name: Lab6.py (use the name the program is
# Course: IT1114/
# Student Name: Laydix Roblero
# Assignment Number: Lab6
# Due Date: 10/11/25
# List specific resources : class mates discussion 

#class work representing an office employee the constructor
class Worker:
    
    def __init__(self):
        self.employee_number = -1
        self.office_number = -1
        self.name = ""
        self.bday = -1
        self.bmonth = -1
        self.byear = -1
        self.hours = 0
        self.overtime = 0

    # Employee number
    def get_employee_number(self):
        return self.employee_number

    def set_employee_number(self, x):
        self.employee_number = x

    # Office number
    def get_office_number(self):
        return self.office_number

    def set_office_number(self, x):
        if x < 100 or x > 500:
            return False
        self.office_number = x
        return True

    # Name
    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x

    # Birthdate
    def get_birthdate(self):
        return f"{self.bday}-{self.bmonth}-{self.byear}"

    def set_birthdate(self, m, d, y):
        if m < 1 or m > 12:
            return False
        if d < 1 or d > 31:
            return False
        self.byear = y
        self.bday = d
        self.bmonth = m
        return True

    # Hours worked
    def get_hours_worked(self):
        return self.hours

    def add_hours(self, x):
        if not isinstance(x, (int, float)):
            return
        if x < 0:
            return
        if x > 9:
            self.hours += 9
            self.overtime += (x - 9)
        else:
            self.hours += x

    def get_hours_overtime(self):
        return self.overtime

               
            
        
            
            

