
class mark:
    # data members
    def read(my):
        global regno, name, malay, science, math
        my.regno = int(input('Enter student registration number'))
        my.name = input('Enter student name')
        my.malay = int(input('Enter malay mark'))
        my.science = int(input('Enter science mark'))
        my.math = int(input('Enter math mark'))

    def display(std):
        total = malay + science + math
        print('Student registration number: ', std.regno)
        print('Student name: ', std.name)
        print('Student malay mark: ', std.malay)
        print('Student science mark: ', std.science)
        print('Student math mark: ', std.math)
        print('Total mark: {} + {} + {} = {} '.format(malay, science, math, total))

# create object for student mark
std1 = mark()
std2 = mark()
std1.read()
std2.read()


# Access the data member values
print ('Student 1 details')
std1.display()
print ('Student 2 details')
std2.display()



