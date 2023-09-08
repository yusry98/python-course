class mark:
  #Data members
  def read(my):
    global regno, name, malay, science, math
    my.regno = int(input('Enter student registration number'))
    my.name = input('Enter student name')
    my.malay = int(input('Enter malay mark'))
    my.science = int(input('Enter science mark'))
    my.math = int(input('Enter math mark'))

  def calc_mark(my):
    global total,avg,result,grade
    total = my.malay + my.science + my.math
    avg = round(total / 3, 2)
    if my.malay >= 50 and my.science >= 50 and my.math >= 50:
        result = 'Pass'
        if avg >= 90:
            grade = 'A+'
        elif avg >= 70:
            grade = 'A'
        elif avg >= 60:
            grade = 'B+'
        elif avg >= 50:
            grade = 'B'
    else:
        result = 'Fail'
        grade = '-'

  def display(self):
    self.calc_mark()
    print('Student registration number: ', self.regno)
    print('Student name: ', self.name)
    print('Student malay mark: ', self.malay)
    print('Student science mark: ', self.science)
    print('Student math mark: ', self.math)
    print('Total mark: {} + {} + {} = {} '.format(self.malay, self.science, self.math, total))
    print('Average mark: ({} + {} + {}) / 3 = {} '.format(self.malay, self.science, self.math, avg))
    print('Result: ', result)
    print('Grade: ', grade)

# create object for student mark
std1 = mark()
std2 = mark()
std3 = mark()
std1.read()
std2.read()
std3.read()

# Access the data member values
print ('Student 1 details')
std1.display()
print ('Student 2 details')
std2.display()
print ('Student 3 details')
std3.display()

