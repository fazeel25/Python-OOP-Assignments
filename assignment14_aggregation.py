class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("John")
dept = Department(emp)
print("Employee in Department:", dept.employee.name)