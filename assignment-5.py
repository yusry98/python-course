# D19P1
s1 = 'Welcome'
s2 = 'to'
s3 = 'Big'
s4 = 'Data'
s5 = 'Class'

s_cont = ' '.join([s1,s2,s3,s4,s5])
print(s_cont)


# D19P2
backtomenu = 'Y'
while backtomenu == 'Y':

    class arithmetic:
        def __init__(self,c,n1,n2):
            self.num1 = n1
            self.num2 = n2
            self.choice = c

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
            else:
                print('Invalid choice')

            backtomenu = input('Do you want to continue press Y otherwise press N: ')
            if backtomenu == 'N':
                print('Thank You')
                exit()
            elif backtomenu != 'Y':
                print('Rejected')
                exit()

    print('1--Addition')
    print('2--Subtraction')
    print('3--Multiplication')
    print('4--Division')
    print('5--Modulus')

    choice = int(input('Enter choice'))

    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))
    arithobj = arithmetic(choice, num1, num2)
    arithobj.check()


# D19P3
list = []
n = int(input("Enter total number of elements : "))
print('Enter the elements:')

for i in range(0, n):
    ele = int(input())
    list.append(ele)
    asc = sorted(list)
    desc = sorted(list, reverse=True)

print('Ascending order')
print(' '.join(map(str, asc)))
print('\n')
print('Descending order')
print(' '.join(map(str, desc)))

# D19P4
# to create employee class
class employee:
    def Getemployee(self, eid, ename, job, age, salary):
        self.empid = eid
        self.empname = ename
        self.empjob  = job
        self.empage = age
        self.basicsalary = salary

    def Calculate(self):
        if self.basicsalary <= 2000:
            self.hra = self.basicsalary * 0.04
            self.ta = self.basicsalary * 0.02
            self.epf = self.basicsalary * 0.09
            self.ins = self.basicsalary * 0.06
        elif self.basicsalary <= 3000:
            self.hra = self.basicsalary * 0.08
            self.ta = self.basicsalary * 0.03
            self.epf = self.basicsalary * 0.09
            self.ins = self.basicsalary * 0.08
        elif self.basicsalary <= 5000:
            self.hra = self.basicsalary * 0.10
            self.ta = self.basicsalary * 0.04
            self.epf = self.basicsalary * 0.11
            self.ins = self.basicsalary * 0.12
        else: 
            self.hra = self.basicsalary * 0.12
            self.ta = self.basicsalary * 0.05
            self.epf = self.basicsalary * 0.12
            self.ins = self.basicsalary * 0.15
            
        self.grosspay = self.basicsalary + self.hra + self.ta
        self.netpay = self.grosspay - (self.epf+self.ins)

    def display_employee(self):
        print('Employee ID: ', self.empid)
        print('Employee Name: ', self.empname)
        print('Employee Age: ', self.empage)
        print('Employee Job: ', self.empjob)
        print('Employee Salary: ', self.basicsalary)
        print('Employee hra: ', self.hra)
        print('Employee epf: ', self.epf)
        print('Employee ta: ', self.ta)
        print('Employee ins: ', self.ins)
        print('Employee grosspay: ', self.grosspay)
        print('Employee netpay: ', self.netpay)

# create object for employee class
empobj = employee()
eid = input('Enter the employee id')
ename = input('Enter the employee name')
salary = int(input('Enter the salary'))
job = input('Enter job name')
age = int(input('Enter the employee age'))

# to call get the employee method
empobj.Getemployee(eid, ename, job, age, salary)
empobj.Calculate()
empobj.display_employee()


# D19P5
def Readstdinfo():
    global regno,name,malay,english
    regno = input('Enter student register no')
    name = input('Enter student name')
    malay = int(input('Enter malay mark'))
    english = int(input('Enter english mark'))
def Calculate():
    global total,average,grade,result
    total = malay + english
    average = total / 2
    if malay >= 50 and english >= 50:
        result = 'Pass'
        if average > 80:
            grade = 'O'
        elif average > 70:
            grade = 'A'
        elif average > 60:
            grade = 'B'
        elif average > 50:
            grade = 'C'
        elif average >= 35:
            grade = 'D'
    else:
        result = 'Fail'
        grade = '-'

def Display():
    print('Student Registered Number: ', regno)
    print('Student Name: ', name)
    print('Malay subject Mark: ', malay)
    print('English subject mark: ', english)
    print('Total mark = ', total)
    print('Average mark = ', average)
    print('Result = ', result)
    print('Grade = ', grade)

Readstdinfo()
Calculate()
Display()
