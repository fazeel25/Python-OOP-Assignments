class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Ali", 50000, "123-45-6789")
print("Name:", emp.name)
print("Protected Salary:", emp._salary)
try:
    print("Private SSN:", emp.__ssn)
except AttributeError:
    print("Private SSN can't be accessed directly")
print("Private SSN accessed using name mangling:", emp._Employee__ssn)