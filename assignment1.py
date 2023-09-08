#D15P1
std_id = int(input('Enter student ID'))
std_fname =input('Enter student firstname')
std_lname = input('Enter student lastname')
std_dob = input('Enter student date of birth')
std_fee = float(input('Enter student fee'))
std_status = input('Is student status active? True / False:')

#D15P2
print(std_id)
print(std_fname)
print(std_lname)
print(std_dob)
print(std_fee)
print(std_status)

#D15P3
try:
    regno = input('Enter student registered number')
    std_fname = input('Enter student firstname')
    std_lname = input('Enter student lastname')

    print('Semester 1 mark: ')
    lib1 = open('library1', 'w')
    s1_malay = int(input('Enter malay marks: '))
    s1_science = int(input('Enter science marks: '))
    s1_maths = int(input('Enter maths marks: '))
    s1_total_marks = s1_malay + s1_science + s1_maths
    lib1.write('Semester 1:'+ '\n'
               + 'Reg no: ' + regno + '\n'
               + 'Student name: ' + std_fname + '\n'
               + 'Student name: ' + std_lname + '\n'
               + 'Malay marks: ' + str(s1_malay) + '\n'
               + 'Science marks: ' + str(s1_science) + '\n'
               + 'Maths marks: ' + str(s1_maths) + '\n'
               + 'Total marks: ' + str(s1_total_marks) + '\n')
    lib1.close()

    print('Semester 2 mark: ')
    lib2 = open('library2', 'w')
    s2_malay = int(input('Enter malay marks: '))
    s2_science = int(input('Enter science marks: '))
    s2_maths = int(input('Enter maths marks: '))
    s2_total_marks = s2_malay + s2_science + s2_maths
    lib2.write('Semester 2:'+ '\n'
               + 'Reg no: ' + regno + '\n'
               + 'Student name: ' + std_fname + '\n'
               + 'Student name: ' + std_lname + '\n'
               + 'Malay marks: ' + str(s2_malay) + '\n'
               + 'Science marks: ' + str(s2_science) + '\n'
               + 'Maths marks: ' + str(s2_maths) + '\n'
               + 'Total marks: ' + str(s2_total_marks) + '\n')
    lib2.close()

    print('Semester 3 mark: ')
    lib3 = open('library3', 'w')
    s3_malay = int(input('Enter malay marks: '))
    s3_science = int(input('Enter science marks: '))
    s3_maths = int(input('Enter maths marks: '))
    s3_total_marks = s3_malay + s3_science + s3_maths
    lib3.write('Semester 3:'+ '\n'
               + 'Reg no: ' + regno + '\n'
               + 'Student name: ' + std_fname + '\n'
               + 'Student name: ' + std_lname + '\n'
               + 'Malay marks: ' + str(s3_malay) + '\n'
               + 'Science marks: ' + str(s3_science) + '\n'
               + 'Maths marks: ' + str(s3_maths) + '\n'
               + 'Total marks: ' + str(s3_total_marks) + '\n')
    lib3.close()

except Exception as ex:
    print(ex)
    print ('You cannot open the file')
finally:
    print('Program End')


#D15P4
try:

    lib1 = open('library1','r')
    for line in lib1:
        print(line)
    lib1.close()

    lib2 = open('library2','r')
    for line in lib2:
        print(line)
    lib2.close()

    lib3 = open('library3','r')
    for line in lib3:
        print(line)
    lib3.close()

except Exception as ex:
    print(ex)
    print('File not available')

finally:
    print('Program End')

#D15P5
# Global variable
university = 'Universiti Sultan Azlan Shah'

def readnew_std():
    global regno,std_name,std_address,std_phone,std_course # Make a local variable as a global access
    regno = int(input('Enter student ID: '))
    std_name = input('Enter student name: ')
    std_address = input('Enter student address: ')
    std_phone = input('Enter student phone number: ')
    std_course = input('Enter student course: ')

def display():
    readnew_std()
    print(university,'New Batch Student')
    print('Student Registered Number: ',regno)
    print('Student Name: ',std_name)
    print('Student Address: ',std_address)
    print('Student Phone Number: ',std_phone)
    print('Student Course: ',std_course)

display()
