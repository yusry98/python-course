# to create employee class
class employee:
    def get_employee(self, eid, ename, salary):
        self.empid = eid
        self.empname = ename
        self.empsalary = salary

    def calculate_salary(self):
        if self.empsalary >= 5000:
            self.hra = self.empsalary * 0.1
            self.epf = self.empsalary * 0.11
            self.ta = self.empsalary * 0.05
            self.ins = self.empsalary * 0.25
            self.sos = 5
        else:
            self.hra = self.empsalary * 0.05
            self.epf = self.empsalary * 0.11
            self.ta = self.empsalary * 0.02
            self.ins = self.empsalary * 0.15
            self.sos = 5

        self.grosspay = self.empsalary + self.hra + self.ta
        self.netpay = self.grosspay - (self.epf+self.ins+self.sos)

    def display_employee(self):
        print('Employee ID: ', self.empid)
        print('Employee Name: ', self.empname)
        print('Employee Salary: ', self.empsalary)
        print('Employee hra: ', self.hra)
        print('Employee epf: ', self.epf)
        print('Employee ta: ', self.ta)
        print('Employee ins: ', self.ins)
        print('Employee sos: ', self.sos)
        print('Employee grosspay: ', self.grosspay)
        print('Employee netpay: ', self.netpay)

# create object for employee class
empobj = employee()
eid = input('Enter the employee id')
ename = input('Enter the employee name')
salary = int(input('Enter the salary'))

# to call get the employee method
empobj.get_employee(eid, ename, salary)
empobj.calculate_salary()
empobj.display_employee()

# constructor
# example 1
class addition:
    def __init__(self):
        self.n1 = 10
        self.n2 = 20

    def result(self):
        print ('Addition of two number = ', self.n1 + self.n2)

addobj = addition()
addobj.result()

# example 2
class addition:
    def __init__(self,f,s):
        self.n1 = f
        self.n2 = s

    def result(self):
        print('Addition of two number = ', self.n1 + self.n2)


addobj = addition(10,20)
addobj.result()

# check given number is odd or even using constructor
class number:
    def __init__(self, n):
        self.num = n

    def check(self):
        if self.num % 2 == 0:
            print('Even number')
        else:
            print('Odd number')

numb = int(input('Enter number'))
numobj = number(numb)
numobj.check()

# Arithmetic operator using constructor

backtomenu = 'y'
while backtomenu == 'y':

    class arithmetic:
        def __init__(self,c,n1,n2):
            self.num1 = n1
            self.num2 = n2
            self.choice = c

        def display_menu(self):
            print('1--Addition')
            print('2--Subtraction')
            print('3--Multiplication')
            print('4--Division')
            print('5--Modulus')
            print('6--Floor Division')

        def check(self):
            if self.choice == 1:
                print('Addition of two number = ', self.num1 + self.num2)
            elif self.choice == 2:
                print('Subtraction of two number = ', self.num1 - self.num2)
            elif self.choice == 3:
                print('Multiplication of two number = ', self.num1 * self.num2)
            elif self.choice == 4:
                print('Division of two number = ', self.num1 / self.num2)
            elif self.choice == 5:
                print('Modulus of two number = ', self.num1 % self.num2)
            elif self.choice == 6:
                print('Floor of two number = ', self.num1 // self.num2)
            else:
                print('Invalid choice')

            backtomenu = input('Do you want to continue press y otherwise press n: ')
            if backtomenu == 'n':
                print('Thank You')
                exit()
            elif backtomenu != 'y':
                print('Rejected')
                exit()

    choice = int(input('Enter choice'))
    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))
    arithobj = arithmetic(choice, num1, num2)
    arithobj.display_menu()
    arithobj.check()

# single inheritance
class a:
    def display(self):
        print('I am from A class')

class b(a):
    def put(self):
        print('I am from B class')

obj = b()
obj.put()
obj.display()

# single inheritance
class student:
    def read(self):
        self.regno = input('Enter student register no')
        self.name = input('Enter student name')
        self.address = input('Enter student address')
    def display(self):
        print(self.regno)
        print(self.name)
        print(self.address)
class mark(student):
    def read_mark(self):
        self.malay = int(input('Enter malay mark'))
        self.english = int(input('Enter english mark'))
        self.science = int(input('Enter science mark'))
        self.total = self.malay + self.english + self.science
        print('Total mark = ', self.total)

obj = mark()
obj.read()
obj.read_mark()
obj.display()

# single inheritance
class father:
    def myfathername (self, fname):
        self.fname = fname
        print(self.fname)

class child(father):
    def myname (self,cname):
        self.cname = cname
        print(self.cname)

childobj = child()
childobj.myname('Yusry')
childobj.myfathername('Zakaria')

# Hierarchy inheritance - one parent more child

class father:
    def myfathername(self, fname):
        self.fname = fname
        print(self.fname)

class child1(father):
    def myname(self, cname):
        self.cname = cname
        print(self.cname)

class child2(father):
    def myname(self, cname):
        self.cname = cname
        print(self.cname)


childobj1 = child1()
childobj1.myname('Dalila')
childobj1.myfathername('Zakaria')
childobj2 = child2()
childobj2.myname('Helmi')
childobj2.myfathername('Zakaria')

# multi-level inheritance

class mygrandfather:
    def mygrandfather(self, fname):
        self.fname = fname
        print(self.fname)

class father(mygrandfather):
    def myfathername(self, fname):
        self.fname = fname
        print(self.fname)

class child1(father):
    def myname(self, cname):
        self.cname = cname
        print(self.cname)

class child2(father):
    def myname(self, cname):
        self.cname = cname
        print(self.cname)

childobj1 = child1()
childobj1.myname('Dalila')
childobj1.myfathername('Zakaria')
childobj1.mygrandfather('Ismail')
childobj2 = child2()
childobj2.myname('Helmi')
childobj2.myfathername('Zakaria')
childobj2.mygrandfather('Ismail')

# multiple inheritance
class mygrandfather:
    def mygrandfather(self, fname):
        self.fname = fname
        print(self.fname)


class father(mygrandfather):
    def myfathername(self, fname):
        self.fname = fname
        print(self.fname)


class child1(father):
    def myname(self, cname):
        self.cname = cname
        print(self.cname)


class child2(father):
    def myname(self, cname):
        self.cname = cname
        print(self.cname)


childobj1 = child1()
childobj1.myname('Dalila')
childobj1.myfathername('Zakaria')
childobj1.mygrandfather('Ismail')
childobj2 = child2()
childobj2.myname('Helmi')
childobj2.myfathername('Zakaria')
childobj2.mygrandfather('Ismail')

# multiple
class father:
    def myfathername(self, fname):
        self.fname = fname
        print(self.fname)

class mother:
    def mymothername(self, mname):
        self.mname = mname
        print(self.mname)

class child(father, mother):
    def myname(self, cname):
        self.cname = cname
        print(self.cname)


childobj = child()
childobj.myname('Yusry')
childobj.myfathername('Zakaria')
childobj.mymothername('Masitah')

"""
Bank detail
1. Create read the customer information and display the customer information using single inheritance
2. Read the customer information and withdraw and deposit amount calculate using hierarchy inheritance

"""

# 1.
class customer:
    def read_cust(self):
        self.account_no = '220201499131'
        self.name = 'Muhammad Yusri'
        self.add = 'Sungai Petani'
        self.balance = 3200

class disp_customer(customer):
    def display_cust(self):
        print('Account number: ',self.account_no)
        print('Account holder: ',self.name)
        print('Address: ',self.add)
        print('Account balance: RM',self.balance)

obj = disp_customer()
obj.read_cust()
obj.display_cust()

#2.
class customer:
    def read_cust(self):
        self.account_no = '220201499131'
        self.name = 'Muhammad Yusri'
        self.add = 'Sungai Petani'
        self.balance = 3200

class depositbycustomer(customer):
    def depo(self):
        self.depo_amount = int(input('Enter depo amount'))
        self.new_balance = self.depo_amount + self.balance
        print('Account number: ', self.account_no)
        print('Account holder: ', self.name)
        print('Address: ', self.add)
        print('Current balance: RM', self.balance)
        print('New Balance : ', self.new_balance)

class withdrawbycustomer(customer):
    def withdraw(self):
        self.withdraw_amount = int(input('Enter withdraw amount'))
        new_balance = self.balance - self.withdraw_amount
        print('Account number: ', self.account_no)
        print('Account holder: ', self.name)
        print('Address: ', self.add)
        print('Current balance: RM', self.balance)
        print('New Balance : ', new_balance)

deposobj = depositbycustomer()
withobj = withdrawbycustomer()
deposobj.read_cust()
deposobj.depo()
withobj.read_cust()
withobj.withdraw()





class A:
  def __init__(self,num): #Constructor
    self.a=num

  def dip_a(self):
    print(self.a)

objA=A(10) #Create object
objA.dip_a()

objA.a=20
objA.dip_a()

objA.a=30
objA.dip_a()


class A:
    def dip_a(self):
        print('Hi, I am parent class -a')


class B(A):
    def dip_a(self):  # Method overriding
        print('Hi, I am child class - a')

    def dip_b(self):
        print('Hi, I am child class - b')


objB = B()  # Create object
objB.dip_a()
objB.dip_b()





