"""
Python File Handling

Till now, we were taking the input from the console and writing it back to the console to interact with the user.

- Sometimes, it is not enough to only display the data on the console.
The data to be displayed may be very large, and only a limited amount of data can be displayed on the console since the memory is volatile,
it is impossible to recover the programmatically generated data again and again.

- The file handling plays an important role when the data needs to be stored permanently into the file.

- A file is a named location on disk to store related information.
 We can access the stored information (non-volatile) after the program termination.

- The file-handling implementation is slightly lengthy or complicated in the other programming language, but it is easier and shorter in Python.

- A file operation can be done in the following order.

-Open a file

-Read or write - Performing operation

-Close the file
"""

"""
Mode
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""

# open an existing file
fp = open('mytxt','r') # open the my txt file
for line in fp: # read content from the file
    print(line)
fp.close() # close the open file

fp = open('mytxt2','r') # open the my txt file
for line in fp: # read content from the file
    print(line)
fp.close() # close the open file

# error handling during the file input output operation
try:
    fp = open('mytxt2', 'r')  # open the my txt file
    for line in fp:  # read content from the file
        print(line)
except IOError:
    print('file is not available')
finally:
    fp.close()

try:
    number = int(input('Enter the number'))
    print(number)
except Exception:
    print('Give valid number')

# division of two numbers using exception
try:
    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))
    print (num1 / num2)
except Exception:
    print('You cannot divide by number 0. Give any valid number.')

# read information from calculation.py python file
fp2 = open('calculation.py','r')
for line in fp2:
    print(line)
fp2.close()

# to create file
try:
    fp = open('simple.txt','w') # create new simple.txt file if not already existing
    fp.write('Yusry\n')
    fp.write('Danial\n')
    fp.write('Yusoof')
except Exception:
    print('You cannot open the file')
finally:
    fp.close()
    print('program end')

# create new file which store numbers one to five
try:
    fp = open('listofnumber.txt', 'w')  # create new simple.txt file if not already existing
    fp.write('1\n')
    fp.write('2\n')
    fp.write('3\n')
    fp.write('4\n')
    fp.write('5')
except Exception:
    print('You cannot open the file')
finally:
    fp.close()
    print('program end')

#
try:
    file_name = input('Enter file name')
    fp = open(file_name, 'w')
    i = 1
    while i <= 5:
        fp.write(str(i)+'\n')
        i += 1
except Exception:
    print('You cannot open the file')
finally:
    fp.close()
    print('program end')

# read the information from file
try:
    file_name = input('Enter file name to be open')
    fp = open(file_name, 'r')
    for line in fp:
        print(line)
except Exception:
    print('Filename is invalid.Try again')
finally:
    fp.close()

# create file to store students name and display the information from file
try:
    file_name = input('Enter file name')
    fp = open(file_name, 'w')
    i = 1
    while i <= 8:
        student_name = input('Enter student name')
        fp.write(str(i)+'. '+student_name+'\n')
        i += 1
except Exception:
    print('You cannot open the file')
finally:
    fp.close()
    print('Eight name of student successfully inserted')
    print('program end')

# Display information from student file
try:
    file_name = input('Enter file name to be open')
    fp = open(file_name, 'r')
    for line in fp:
        print(line)
except Exception:
    print('Filename is invalid.Try again')
finally:
    fp.close()

# update the content to the existing file
fp = open('student_name.txt','a')
fp.write('Dayana\n')
fp.write('Huda')
fp.close()
fp = open('student_name.txt','r')
for i in fp:
    print(i)
fp.close()

# remove an existing file
import os
os.remove('simple.txt')

import os
try:
    if os.path.exists('student_name.txt'):
        os.remove('student_name.txt')
        print('File successfully deleted')
    else:
        print('File is not available. Try to give valid file name')
except Exception as e:
    print('Exception occurs: ', e)
    print('Not able to delete the file')
finally:
    print('end')

# to create directory / folder
import os
os.mkdir('Wong')

# remove
os.rmdir('Wong')
os.rmdir('yusry')

#
fp = open('mytxt','r')
ch = fp.read(21)
print(ch)
position = fp.tell() # use to know position of the cursor
print(position)
fp.seek(10) # used to move the cursor to the exact position
ch = fp.read(5)
print(ch)
position = fp.tell()
print(position)
fp.close()

# Create the file which is store the patient information
"""
1. create new file
2. Store 10 patient information 
    100 Yusry 24 0919922902 KL 09:00 12:17 2022-08-15 
3. Update two more information into the file
4. Display the content from the file
5. Searching patient information available or not
6. Remove the file 
"""

backtomenu = 'y'
while backtomenu == 'y' or backtomenu == 'Y':

    print('1--> Create new file')
    print('2--> Store 10 patient information')
    print('3--> Update two more information into the file')
    print('4--> Display the content from the file')
    print('5--> Searching patient information available or not')
    print('6--> Remove the file')

    choice = int(input('Enter your choice'))

    if choice == 1:
        try:
            file_name = input('Enter file name')
            fp = open(file_name, 'w')
            print('File successfully created')
        except Exception:
            print('You cannot open the file')
        finally:
            fp.close()
            print('Program end')
    elif choice ==2:
        try:
            file_name = input('Enter file name')
            fp = open(file_name, 'w')
            i = 1
            while i <= 2:
                pid= input('Enter patient ID')
                p_name = input('Enter patient name')
                p_age = input('Enter patient age')
                p_add = input('Enter patient address')
                p_phono = input('Enter patient phone number')
                checkin_time = input('Enter patient check in time')
                checkout_time= input('Enter patient check out time')
                adm_date = input('Enter patient admission date')
                fp.write(pid + ' '
                         + p_name + ' '
                         + p_age + ' '
                         + p_add + ' '
                         + p_phono + ' '
                         + checkin_time + ' '
                         + checkout_time + ' '
                         + adm_date +'\n')
                i += 1
        except Exception:
            print('You cannot open the file')
        finally:
            fp.close()
            print('Successfully added 10 patient information')
            print('Program end')
    elif choice == 3:
        try:
            file_name = input('Enter file name')
            fp = open(file_name, 'a')
            i = 1
            while i <= 2:
                patient_info = input('Enter patient info')
                fp.write(patient_info + '\n')
                i += 1
        except Exception:
            print('You cannot open the file')
        finally:
            fp.close()
            print('Successfully added two more patient information')
            print('Program end')
    elif choice == 4:
        try:
            file_name = input('Enter file name to be open')
            fp = open(file_name, 'r')
            for line in fp:
                print(line)
        except Exception:
            print('Filename is invalid.Try again')
        finally:
            fp.close()
    elif choice == 5:
        try:
            file_name = input('Enter file name to be open')
            fp = open(file_name, 'r')
            key = input('Search the patient info')
            for line in fp:
                if key in line:
                    print('{} is available in the list'.format(key))
                    break
            else:
                print('{} is not available in the list'.format(key))
        except Exception:
            print('Filename is invalid.Try again')
        finally:
            fp.close()
    elif choice == 6:
        try:
            file_name = input('Enter file name to be remove')
            import os
            os.remove(file_name)
        except Exception:
            print('Filename is invalid. Try again')
        finally:
            print('Successfully removed')
    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n' or backtomenu == 'N':
        print('Thank You')
        exit()
    elif backtomenu != 'y' and backtomenu != 'Y':
        print('Rejected')
        exit()

