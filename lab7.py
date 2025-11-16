# Program Name: Lab7.py (use the name the program is
# Course: IT1114/
# Student Name: Laydix Roblero
# Assignment Number: Lab6
# Due Date: 10/17/25
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

        self.hours = 0.0
        self.overtime = 0.0
        #pay
        self.hourly_salary = 0.0
        self.overtime_salary = 0.0

    # Employee number
    def get_employee_number(self):
        return self.employee_number

    def set_employee_number(self, x):
        if not isinstance(x, int):
            return False
        self.employee_number = x
        return True

    # Office number
    def get_office_number(self):
        return self.office_number

    def set_office_number(self, x):
        if not isinstance(x, int):
            return False
        if x < 100 or x > 500:
            return False
        self.office_number = x
        return True

    # Name
    def get_name(self):
        return self.name

    def set_name(self, x):
        if not isinstance(x, str):
            return False
        self.name = x
        return True

    # Birthdate
    def get_birthdate(self):
        return f"{self.bday}-{self.bmonth}-{self.byear}"

    def set_birthdate(self, month, day, year):
        ok = all(isinstance(v, int) for v in (month, day, year))
        if not ok:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if year < 1900 or year > 2100:
            return False
        self.bmonth, self.bday, self.byear = month, day, year
        return True

    def get_birthdate(self):
        return f"{self.bmonth}/{self.bday}/{self.byear}"


    # Hours worked
    def get_hours_worked(self):
        return self.hours

    def add_hours(self, x):
        if not isinstance(x, (int, float)):
            return False
        if x < 0:
            return False 
        reg = min(x, 9)
        ot = max(0.0, x - 9)
        self.hours += reg
        self.overtime += ot
        return True

    def get_hours_overtime(self):
        return self.overtime

    def set_hourly_salary(self, x):
        if not isinstance(x, (int, float)):
            return False
        if x < 0:
            return False
        self.hourly_salary = float(x)
        return True
    def get_hourly_salary(self):
        return self.hourly_salary

    def set_overtime_salary(self, x):
        if not isinstance(x, (int, float)):
            return False
        if x < 0:
            return False
        self.overtime_salary = float(x)
        return True


    def get_overtime_salary(self):
        return self.overtime_salary

    def get_pay(self):
        return (self.hours * self.hourly_salary) + (self.overtime * self.overtime_salary)
