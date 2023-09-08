class Student:

    def __init__(myself, rollno, name, age):
        myself.rollno = rollno
        myself.name = name
        myself.age = age

    def display(myself):
        print(myself.rollno,myself.name,myself.age)

std = Student(101,'Yusry',24)
std.display()
# You can modify properties on objects
std.name = 'Yusri'
std.display()

# Delete object Properties
# You can delete properties on objects by using the del keyword
del std.age # delete age property
del std # delete object


# Empty class
class Employee:
    pass

# create student class with rollno attribute


# To create employee class
class employee:
    # Data members
    empid = 101
    empname = 'wong'
    salary = '3500'

    def display(self):
        print('Employee id : ',self.empid)
        print('Employee Name: ',self.empname)
        print('Employee Salary: ', self.salary)

# create object for employee class
emp = employee()
print(type(emp))

# access the data member values
emp.display()



# To create employee class
class employee:
    # Data members
    def read(self):
        self.empid = int(input('Enter the employee ID'))
        self.empname = input('Enter the employee name')
        self.salary = float (input('Enter the employee salary'))

    def display(self):
        print('Employee id: ',self.empid)
        print('Employee Name: ', self.empname)
        print('Employee Salary: ', self.salary)

# create object for employee class
emp = employee()
emp2 = employee()
emp3 = employee()

#print(type(emp)
