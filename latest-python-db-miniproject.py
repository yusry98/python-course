"""
Database structure
table name: PHCDC_StudentPersonal
column:
student_id      varchar(10)   primary key
student_fname   varchar(50)   not null
student_lname   varchar(50)   not null
student_ic      varchar(14)   not null    unique
student_address varchar(30)   not null
student_city    varchar(25)   not null
student_postal_code varchar(6)   not null
student_state   varchar(25)   not null
student_email   varchar(30)     not null
student_phone   varchar(14)     not null
"""

"""
table name: PHCDC_StudentMark
column:
student_id       varchar(10)   foreign key
assignment_mark  int           not null and check <= 10
miniproject_mark int           not null and check <= 25 
test_mark        int           not null and check <= 65
total_mark       int  
result           varchar(4)    not null and check pass or fail          
grade            varchar(2)    not null
"""

"""
PHCDC Student Management - Mini Project
1. Insert new student personal information 
2. Display the student personal information 
3. Edit student personal information 
    a. Modify student fname
    b. Modify student lname
    c. Modify student ic
    d. Modify student address
    e. Modify student postal code
    f. Modify student state
    g. Modify student email
    h. Modify student phone
4. Insert student mark
5. Display the student result  # get input from student_id after display the student_id, student_name and result pass or fail
6. Generate mark sheet 
output = student_id  student_ic  student_name  assignment_mark  miniproject_mark  test_mark  total_mark  result  grade
"""

backtomenu = 'y'
while backtomenu == 'y':

    print('1--> Insert new student personal information')
    print('2--> Display the student personal information')
    print('3--> Modify student personal information')
    print('4--> Insert student mark')
    print('5--> Display the student result')
    print('6--> Generate mark sheet')

    import pyodbc
    # establish connection
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                          'Database={PHCDC2022};'
                          'Trusted_Connection=yes;')
    conn.autocommit = True  # permenantly store all the transaction on the server
    cursor = conn.cursor()  # initialization of the cursor

    choice = int(input('Enter your choice'))

    if choice == 1:
        std_id = input('Student ID : ')
        std_fname = input('Student Firstname : ')
        std_lname = input('Student Lastname : ')
        std_ic = input('Student IC : ')
        std_add = input('Student Address : ')
        std_city = input('Student City : ')
        std_postal = input('Student Postal : ')
        std_state = input('Student State : ')
        std_email = input('Student Email : ')
        std_phono = input('Student Phone Number : ')

        cursor.execute("Insert PHCDC_StudentPersonal(student_id,student_fname,student_lname,student_ic,student_add,student_city,student_postal,student_state,student_email,student_phono) VALUES (?,?,?,?,?,?,?,?,?,?)",
                       (std_id,std_fname,std_lname,std_ic,std_add,std_city,std_postal,std_state,std_email,std_phono))
        print('Record has been inserted successfully')

    elif choice == 2:
        cursor.execute("SELECT * FROM PHCDC_StudentPersonal")
        result = cursor.fetchall()
        # print(type((result)))
        for x in result:
            print(x)

    elif choice == 3:
        uid = input('Enter Student ID')
        cursor.execute("SELECT * FROM PHCDC_StudentPersonal where student_id = ?", uid)
        result = cursor.fetchall()
        # print(type((result)))
        for x in result:
            if uid in x:
                print('1--> Modify student firstname')
                print('2--> Modify student lastname')
                print('3--> Modify student IC')
                print('4--> Modify student address')
                print('5--> Modify student city')
                print('6--> Modify student postal')
                print('7--> Modify student state')
                print('8--> Modify student email')
                print('9--> Modify student phone number')

                modify = int(input('Enter your choice'))

                if modify == 1:
                    std_fname = input('Change firstname to : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_fname = ? where student_id = ?;",
                                   std_fname, uid)
                    print('Record has been updated successfully')

                elif modify == 2:
                    std_lname = input('Change lastname to : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_lname = ? where student_id = ?;",
                                   std_lname, uid)
                    print('Record has been updated successfully')

                elif modify == 3:
                    std_ic = input('Change student IC to : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_ic = ? where student_id = ?;", std_ic, uid)
                    print('Record has been updated successfully')

                elif modify == 4:
                    std_add = input('Change address to : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_add = ? where student_id = ?;", std_add,
                                   uid)
                    print('Record has been updated successfully')

                elif modify == 5:
                    std_city = input('Change city to : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_city = ? where student_id = ?;", std_city,
                                   uid)
                    print('Record has been updated successfully')

                elif modify == 6:
                    std_postal = input('Change postal to : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_postal = ? where student_id = ?;",
                                   std_postal, uid)
                    print('Record has been updated successfully')

                elif modify == 7:
                    std_state = input('Change state tu : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_state = ? where student_id = ?;",
                                   std_state, uid)
                    print('Record has been updated successfully')

                elif modify == 8:
                    std_email = input('Change email to : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_email = ? where student_id = ?;",
                                   std_email, uid)
                    print('Record has been updated successfully')

                elif modify == 9:
                    std_phono = input('Change phone number to : ')
                    cursor.execute("update PHCDC_StudentPersonal set student_phono = ? where student_id = ?;",
                                   std_phono, uid)
                    print('Record has been updated successfully')
                else:
                    print('Invalid choice')
                break
        else:
            print('Student not available')

    elif choice == 4:
        std_id = input('Student ID : ')
        assignment_m = int(input('Assignment mark : '))
        miniproject_m = int(input('Mini Project mark : '))
        test_m = int(input('Test mark : '))
        total_m = assignment_m + miniproject_m + test_m
        if total_m >= 50:
            result = 'Pass'
            if total_m >= 90:
                grade = 'A+'
            elif total_m >= 80:
                grade = 'A'
            elif total_m >= 70:
                grade = 'B+'
            elif total_m >= 60:
                grade = 'B'
        else:
            result = 'Fail'
            grade = '-'

        cursor.execute("Insert PHCDC_StudentMark(std_id,assignment_mark,miniproject_mark,test_mark,total_mark,result,grade) VALUES (?,?,?,?,?,?,?)",(std_id, assignment_m, miniproject_m, test_m, total_m, result, grade))
        print('Record has been inserted successfully')

    elif choice == 5:
        uid = input('Enter Student ID')
        cursor.execute("SELECT student_id,student_fname,result FROM PHCDC_StudentPersonal LEFT JOIN PHCDC_StudentMark ON PHCDC_StudentPersonal.student_id=PHCDC_StudentMark.std_id where student_id = ?", uid)
        result = cursor.fetchall()
        # print(type((result)))
        for x in result:
            if uid in x:
                print(x)
                break
        else:
            print('No record found')

    elif choice == 6:
        cursor.execute("SELECT * FROM PHCDC_StudentPersonal LEFT JOIN PHCDC_StudentMark ON PHCDC_StudentPersonal.student_id=PHCDC_StudentMark.std_id")
        result = cursor.fetchall()
        # print(type((result)))
        for x in result:
            print(x)

    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()

