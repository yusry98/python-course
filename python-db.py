"""
pyodbc is an open source Python module that makes accessing ODBC databases simple pyodbc is going to be the bridge between SQL and Python. This makes access easy to ODBC (Open Database Connectivity) databases

Python SQL Connector Module Methods

connect(): This function is used for establishing a connection with the SQL server. The following are the arguments that are used to initiate a connection:

user: User name associated with the MySQL server used to authenticate the connection
password: Password associated with the user name for authentication
database: Data base in the SQL Server for creating the Table

cursor(): Cursor is the workspace created in the system memory when the SQL command is executed. This memory is temporary and the cursor connection is bounded for the entire session/lifetime and the commands are executed

execute(): The execute function takes a SQL query as an argument and executes. A query is an SQL command which is used to create, insert, select, update, delete etc.

"""

# Establish the connection between Python and Databases

import pyodbc  # import section

# connection string
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=hotel_management_system;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
print('Connection successfully established')

"""
Driver=SQL Server;Server=ServerName;Database=DatabaseName; Trusted_Connection=Yes;**

-Driver=SQL Server specifies that Microsoft SQL Server is the driver for this connection.

-Server=ServerName specifies that ServerName is the name of the server to which the connection is established.

-Database=DatabaseName  specifies that DatabaseName is the name of the data source.

- Trusted_Connection=Yes specifies that a user account<2> is used to establish this connection.

Reference:https://docs.microsoft.com/en-us/openspecs/sql_server_protocols/ms-odbcstr/864608a0-29e9-4766-9505-58c336bcd762

"""

# create own database
import pyodbc

# establish connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                      'Database={hotel_management_system};'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permenantly store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Create database YZakaria")
print('Database has been created successfully')

# create table
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Create table MyTable(UserID int primary key, Password varchar(30)")
print('Table has been created successfully')

# insert record in table
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
# conn.autocommit = True # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Insert MyTable values(104, '123abc')")
cursor.execute("Insert MyTable values(105, '456abc')")
cursor.execute("Insert MyTable values(106, '789abc')")
print('Record has been inserted successfully')
conn.commit()

# read data from user and store into the table
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
uid = int(input('Enter user ID'))
password = input('Enter your name')
# conn.autocommit = True # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("INSERT INTO MyTable(UserID, Password) VALUES (?,?)", (uid, password))
print('Record has been inserted successfully')
conn.commit()

# delete data from table
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
# conn.autocommit = True # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("delete MyTable where UserID = 101")
print('Record has been deleted successfully')
conn.commit()

# update data from table
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
# conn.autocommit = True # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("update MyTable set Password = 'yusry123' where userID = 102")
print('Record has been updated successfully')
conn.commit()

# fetch all data from table
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
# conn.autocommit = True # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("select * from MyTable")
result = cursor.fetchall()
# print(type((result)))
for x in result:
    print(x)
# print(type(x)) # row datatype
conn.commit()

# create multiple table
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Create table Employee(EmpId int primary key, EmpName varchar(30), EmpJob varchar(30), EmpSalary float)")
cursor.execute("Create table Student(StudentId int primary key, StudentName varchar(30), StudentEmail varchar(30))")
cursor.execute(
    "Create table Patient(PatientId int primary key, PatientName varchar(30), PatientAge int, Diesease varchar(30))")
print('Multiple table has been created successfully')

# drop table
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
# conn.autocommit = True # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Drop table Patient")
print('Table has been deleted successfully')
conn.commit()  # permanently store all the transaction on the server

# drop database if database is empty can delete otherwise cannot delete
import pyodbc

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
# conn.autocommit = True # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Drop database YusryZa")
print('Database has been drop successfully')
conn.commit()  # permanently store all the transaction on the server

# 21 Jun 2022
# delete the record using exception handling
import pyodbc

# establish
try:
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                          'Database=YusryZa;'
                          'Trusted_Connection=yes;')
    conn.autocommit = True  # permanently store all the transaction on the server
    cursor = conn.cursor()  # initialization of the cursor
    uid = int(input("-- Please enter id of employee"))
    # password = (input("-- Please enter the password of employee "))
    # cursor.execute("Delete YusryZa.dbo.MyTable where UserID = %d or Password ='%s'" %(uid, password))
    #key = cursor.execute("Select UserID from MyTable where userID = %d" % (uid))
    #cursor.execute("Select UserID from MyTable where UserID = %d" % (uid))
    cursor.execute("Select UserID from MyTable")
    result = cursor.fetchall()
    uidlist = [i[0] for i in result]
    #print(uidlist)
    if uid in (uidlist):
        print('Employee is available')
    else:
        print('Employee is not available')
except Exception as ex:
    print('Connection error:', ex)
finally:
    conn.close()

uid = input('Enter Student ID')
cursor.execute("SELECT * FROM PHCDC_StudentPersonal where student_id = ?", uid)
result = cursor.fetchall()
# print(type((result)))
for x in result:
    if uid in x:
        print(x)
        break
    else:
        print('No record found')



# to import matplotlib
import matplotlib

# to display version of matplotlib
print(matplotlib.__version__)

#
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 20])
y = np.array([0, 200])

plt.plot(x, y)
plt.show()

#
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 5])
y = np.array([10, 50])

plt.plot(x, y)
plt.show()

#
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# plotting without x-points
# if we do not specify the points in the x-axis, they will get the default values 0,1,2,3,4,5
#

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# Matplotlib Markers
"""
Marker	Description
'o'	    Circle	
'*'	    Star	
'.'	    Point	
','	    Pixel	
'x'	    X	
'X'	    X (filled)	
'+'	    Plus	
'P'	    Plus (filled)	
's'	    Square	
'D'	    Diamond	
'd'	    Diamond (thin)	
'p'	    Pentagon	
'H'	    Hexagon	
'h'	    Hexagon	
'v'	    Triangle Down	
'^'	    Triangle Up	
'<'	    Triangle Left	
'>'	    Triangle Right	
'1'	    Tri Down	
'2'	    Tri Up	
'3'	    Tri Left	
'4'	    Tri Right	
'|'	    Vline	
'_'	    Hline

"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints, marker='*')
plt.show()

#
"""
Line Reference
Line Syntax	  Description
'-'	          Solid line	
':'	          Dotted line	
'--'	        Dashed line	
'-.'	        Dashed/dotted line

Color Reference
Color Syntax	Description
'r'	          Red	
'g'	          Green	
'b'	          Blue	
'c'         	Cyan	
'm'	          Magenta	
'y'	          Yellow	
'k'	          Black	
'w'	          White

"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:b')
plt.show()

# Marker size
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20)
plt.show()

# Marker color
# Set the EDGE color to blue

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20, mec='r')
plt.show()

#

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20, mec='r')
plt.show()

# 22 Jun 2022

# student mark list report
# database structure


import pyodbc
import matplotlib.pyplot as plt

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("drop table mystudent")
cursor.execute("Create table mystudent (student_id int,fname varchar(20),lname varchar(20),english int,maths int,science int,total as (english + maths + science))")
print('Table has been created successfully')
total_student = int(input('Enter total number of student to be inserted'))
for i in range(total_student):
    s_id = int(input('Enter the student id'))
    s_fname = input('Enter student firstname')
    s_lname = input('Enter student lastname')
    english_mark = int(input('Enter English mark'))
    maths_mark = int(input('Enter Maths mark'))
    science_mark = int(input('Enter Science mark'))
    cursor.execute("Insert mystudent Values(%d,'%s','%s', %d, %d, %d)" % (
    s_id, s_fname, s_lname, english_mark, maths_mark, science_mark))
    print('Student {} record successfully inserted'.format(i))
print('Student details')
cursor.execute("select * from mystudent")
result = cursor.fetchall()
# print(type((result)))
for x in result:
    print(x)

cursor.execute("select fname, total from mystudent")
result = cursor.fetchall()
name = [i[0] for i in result]
total = [i[1] for i in result]
print(name)
print(total)
x = name
y = total
xlabel = [i[0] for i in result]
print(xlabel)
colors = ['yellow', 'red', 'pink','black']
plt.pie(y, labels=xlabel, colors=colors)
plt.legend(title = "Student total mark")
plt.show()
conn.close()

#plt.bar(x,y,tick_label=xlabel,width=0.3,color=['red','yellow','blue'])
#plt.bar(x,y,tick_label=xlabel,width=0.2, color=['red','yellow'])

#plt.bar(x,y,tick_label=xlabel,width=0.3,color=['red','yellow','blue'])
#plt.title('Students mark details')
#plt.xlabel('Students name')
#plt.ylabel('Student total mark')




# employee salary details
import pyodbc
import matplotlib.pyplot as plt

# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=YusryZa;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("drop table employee_salary")
cursor.execute("Create table employee_salary(employee_id int,employee_name varchar(30),employee_age int,employee_job varchar(20),salary int)")
print('Table has been created successfully')
total_employee = int(input('Enter total number of employee to be inserted'))
for i in range(total_employee):
    emp_id = int(input('Enter the employee id'))
    emp_name = input('Enter the employee name')
    emp_age = int(input('Enter the employee age'))
    emp_job = input('Enter the employee job name')
    emp_salary = int(input('Enter the employee salary'))
    cursor.execute("Insert employee_salary Values(%d,'%s',%d, '%s', %d)" % (emp_id, emp_name, emp_age, emp_job, emp_salary))
    print('Student {} record successfully inserted'.format(i))
print('Employee salary details')
cursor.execute("select * from employee_salary")
result = cursor.fetchall()
# print(type((result)))
for x in result:
    print(x)

cursor.execute("select employee_name, salary from employee_salary")
result = cursor.fetchall()
name = [i[0] for i in result]
salary = [i[1] for i in result]
print(name)
print(salary)
x = name
y = salary
colors = ['yellow', 'red', 'pink','black']
plt.pie(y, labels=xlabel, colors=colors)
plt.legend(title = "Employee Salary")
plt.show()
conn.close()





