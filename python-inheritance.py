"""
Inheritance allows us to define a class that inherits all the methods and properties from
another class. Parent class is the class being inherited from, also called a base class.
Child class is the class that inherits from another class, also called derived class.
"""

# create a Parent Class
# example 1:
class Person: # Parent class
    def __init__ (self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person): # child class
    pass

x = Student('Yusry','Zakaria')
x.printname()

# example:2
class Person: # Parent class
    def __init__ (self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__ (self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student('Yusry','Zakaria','2019')
x.printname()
print(x.graduationyear)


# Parent class
class FulltimeEmp:
    def __init__(self, name, age):  # Automatically initialize attributes
        self.name = name
        self.age = age
    def info(self):
        print(f"Employee. My name is {self.name}. "
              f"I am {self.age} years old.")
    def EPF(self):
        print("EPF is deducted for my Salary")

# Child class
class ParttimeEmp(FulltimeEmp):
    def __init__(self, name, age):
        FulltimeEmp.__init__(self, name, age)  # Automatically invoke the parent class init method
    def EPF(self):
        print("EPF is not deducted for my Salary")

# Creating Objects of the Class
E1 = FulltimeEmp("Mr. Aysraf", 26)
E2 = ParttimeEmp("Mr. Phan", 44)

for persons in (E1, E2):
    persons.info()
    persons.EPF()


# Create Class
class Addition:
    first = 0
    second = 0
    answer = 0
    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s
    def display(self):
        print("First number = " + str(self.first))
        # print("First number = ",self.first)
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
    def calculate(self):
        self.answer = self.first + self.second
# creating object of the class
obj = Addition(10, 20)
# perform Addition
obj.calculate()
# display result
obj.display()


# Create Class
class Addition:
    # parameterized constructor
    def __init__(self):
        self.first = int(input('Enter first number'))
        self.second = int(input('Enter second number'))
    def display(self):
        print("First number = " + str(self.first))
        # print("First number = ",self.first)
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
    def calculate(self):
        self.answer = self.first + self.second
# creating object of the class
obj = Addition()
# perform Addition
obj.calculate()
# display result
obj.display()


# Create Class
class Addition:
    # parameterized constructor
    def __init__(self,n1,n2):
        self.first = n1
        self.second = n2
    def display(self):
        print("First number = " + str(self.first))
        # print("First number = ",self.first)
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
    def calculate(self):
        self.answer = self.first + self.second
# creating object of the class
n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))
obj = Addition(n1,n2)
# perform Addition
obj.calculate()
# display result
obj.display()


# Division of two numbers - Default constructor(no parameter passing)
# Create Class
class Division:
    first = 0
    second = 0
    answer = 0

    # default constructor - no parameter
    def __init__(self):
        self.first = 10
        self.second = 2

        """
        self.first = int(input("Enter first number"))
        self.second = int(input("Enter second number"))

        """

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Division of two numbers = " + str(self.answer))

    def calculate(self):
        # try:
        self.answer = self.first / self.second
        # except Exception:
        # print("Cannot Divid / zero Exception occurs")


# creating object of the class
# this will invoke default constructor
obj = Division()
# perform Division
obj.calculate()

# display result
obj.display()
