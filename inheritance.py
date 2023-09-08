# Python program to demonstrate
"""Single inheritance: When a child class inherits from only one parent class, 
it is called single inheritance
"""

class Parent:  # Parent class
    def func1(self):
        print("This function is in parent class.")
# Derived class
class Child(Parent):  # Child class
    def func2(self):
        print("This function is in child class.")
# Driver's code
object = Child()
object.func1()  # Reuse parent class func1()
object.func2()  # Call func2() in child class

#Create python program to perform arithmetic operation using single inheritance

class Readnum: #Parent class
  def __init__(self,f,s):#parameterized constructor
    self.first=f
    self.second=s

  def displaynumber(self):
    print("First number is",self.first)
    print("Second number is",self.second)

# Create python program to perform arithmetic operation using single inheritance
class Myarithmetic(Readnum):  #Child/Derived class
 # def __init__(self,f,s):
     #  Readnum.__init__(self,f,s)
  def arith_operations(self):
    print("Addition value is",self.first+self.second)
    print("Subtraction value is",self.first-self.second)
    print("Multiplication value",self.first*self.second)
    print("Division value",self.first/self.second)
    print("Modulus value",self.first%self.second)

num1=int(input("Enter First number"))
num2=int(input("Enter Second number"))

op=Myarithmetic(num1,num2) #create object for child class
print()
op.displaynumber() #Invoke parent class method
print("\nArithmetic Operations")
print("---------------------")
op.arith_operations() #Invoke child class method

# Python program to demonstrate
"""
Multiple inheritance:When a child class inherits from multiple parent classes, 
it is called multiple inheritance
"""
# Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
# Base class2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
# Driver's code
s1 = Son()
s1.fathername = "Vikram"
s1.mothername = "Viji"
s1.parents()


# Python program to demonstrate
# Multilevel inheritance: When we have a child and grandchild relationship.

# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)

# Derived/child class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

#  Driver code
s1 = Son('Krishna', 'Raj', 'Samy')
print(s1.grandfathername)
s1.print_name()


# Python program to demonstrate
# Hierarchical inheritance: More than one derived classes are created from a single base class

# Base class
class Parent:
    def func1(self):
        print("Hi I am Parent class method")
# Derived class1
class Child1(Parent):
    def func2(self):
        print("Hi I am Child 1 class method")
# Derivied class2
class Child2(Parent):
    def func3(self):
        print("Hi I am Child 2 class method")
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# Python program to demonstrate
"""
Hybrid inheritance: This form combines more than one form of inheritance. Basically, 
it is a blend of more than one type of inheritance.
"""
class School:  # Parent class
    def func1(self):
        print("Hi I am a method in school class")
class Student1(School):  # Single inheritance
    def func2(self):
        print("Hi I am method in student 1 class ")
class Student2(School):  # Single inheritance
    def func3(self):
        print("Hi i am a method in student 2 class")
class Student3(Student1, School):  # Multiple inheritance
    def func4(self):
        print("Hi i am a method in student 3 class")
# Driver's code
object = Student3()
object.func1()
object.func2()
# object.func3() cannot access func3() not attribute of Student3 class
object.func4()
