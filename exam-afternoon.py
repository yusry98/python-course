import pyodbc
import numpy as np
import matplotlib.pyplot as plt

# connect to python
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                      'Database={yusry_phcdc};'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permenantly store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor

backtomenu = 'y'
while backtomenu == 'y':

    print('1--> Modify/Update Maths Mark')
    print('2--> Modify/Update Science Mark')
    print('3--> Modify/Update English Mark')
    print('4--> Generate Maths Mark Graph')
    print('5--> Generate Science Mark Graph')
    print('6--> Generate English Mark Graph')

    choice = int(input('Enter your choice'))

    if choice == 1:
        sid = int(input('Enter student rollno to edit'))
        update_maths = float(input('Change Maths mark to : '))
        cursor.execute("update usas_student_mark set math = ? where std_rollno = ?;", update_maths, sid)
        print('Record has been updated successfully')

    elif choice == 2:
        sid = int(input('Enter student rollno to edit'))
        update_science = float(input('Change Science mark to : '))
        cursor.execute("update usas_student_mark set science = ? where std_rollno = ?;", update_science, sid)
        print('Record has been updated successfully')

    elif choice == 3:
        sid = int(input('Enter student rollno to edit'))
        update_english = float(input('Change English mark to : '))
        cursor.execute("update usas_student_mark set english = ? where std_rollno = ?;", update_english, sid)
        print('Record has been updated successfully')

    elif choice == 4:
        try:
            cursor.execute("SELECT std_rollno,math FROM usas_student_mark")
            result = cursor.fetchall()

            x = np.array([x[0] for x in result])
            y = np.array([x[1] for x in result])

            plt.bar(x, y, color="green", width=0.5)

            plt.title("Maths Mark Bar Graph Report")
            plt.xlabel("Student ID")
            plt.ylabel("Maths Mark")

            plt.show()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()

    elif choice == 5:
        try:
            cursor.execute("SELECT std_rollno,science FROM usas_student_mark")
            result = cursor.fetchall()

            x = np.array([x[0] for x in result])
            y = np.array([x[1] for x in result])

            plt.bar(x, y, color="blue", width=0.5)

            plt.title("Science Mark Bar Graph Report")
            plt.xlabel("Student ID")
            plt.ylabel("Science Mark")

            plt.show()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()

    elif choice == 6:
        try:
            cursor.execute("SELECT std_rollno,english FROM usas_student_mark")
            result = cursor.fetchall()

            x = np.array([x[0] for x in result])
            y = np.array([x[1] for x in result])

            plt.bar(x, y, color="red", width=0.5)

            plt.title("English Mark Bar Graph Report")
            plt.xlabel("Student ID")
            plt.ylabel("English Mark")

            plt.show()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()

    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()



# update database using python

# Maths mark


# Science mark


# English mark



# display graph using python
