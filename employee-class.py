# Example 1: To create employee class
class employee:
  # Data members
  empid = 101
  empname = 'wong'
  salary = '3500'

# create object for employee class
emp = employee()

# Access the data member values
print('Employee id :', emp.empid)
print('Employee Name :', emp.empname)
print('Employee Salary :', emp.salary)

# Example 2: To create employee class
class employee:
  # Data members
  empid = 101
  empname = 'wong'
  salary = '3500'

  def display(self): # create method to display employee details
    print('Employee id : ', self.empid)
    print('Employee Name: ', self.empname)
    print('Employee Salary: ', self.salary)

# create object for employee class
emp = employee()

# Access the data member values
emp.display()

# Example 3: To create employee class
class employee:
  #Data members
  def read(my): #Create method to read employee details and assign the employee data members
    my.empid=int(input('Enter the employee ID'))
    my.empname = input('Enter the employee name')
    my.salary1 = float(input('Enter the emplyee salary'))
    my.salary2 = float(input('Enter the emplyee salary'))

  def calc_salary(my):
    global total
    total = my.salary1 + my.salary2


  def display(self): #Create method to display employee details
    self.calc_salary()
    print('Employee id : ',self.empid)
    print('Employee Name : ',self.empname)
    print('Employee Salary : ',self.salary1)
    print('Employee Salary : ', self.salary2)
    print('Total mark: {} + {} = {} '.format(self.salary1, self.salary2, total))


#Create object for employee class
emp=employee()
emp2=employee()
emp3=employee()
#print(type(emp))
emp.read()
emp2.read()
emp3.read()
#Access the data member values
print('Employee 1 details')
emp.display()
print('Employee 2 details')
emp2.display()
print('Employee 3 details')
emp3.display()

