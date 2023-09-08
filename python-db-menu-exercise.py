
backtomenu = 'y'
while backtomenu == 'y':

    print('1--> Create database')
    print('2--> Create table')
    print('3--> Insert record into MyTable')
    print('4--> Fetch all data from table')
    print('5--> Delete record from MyTable')
    print('6--> Delete all record')
    print('7--> Delete table')
    print('8--> Drop database')

    import pyodbc
    # establish connection
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                          'Database={YusryZa};'
                          'Trusted_Connection=yes;')
    conn.autocommit = True  # permenantly store all the transaction on the server
    cursor = conn.cursor()  # initialization of the cursor

    choice = int(input('Enter your choice'))

    if choice == 1:
        db_name = input('Enter database name')
        cursor.execute("Create database {};".format(db_name))
        print('Database has been created successfully')

    elif choice == 2:
        table_name = input('Enter table name')
        cursor.execute("Create table {} (UserID int, Password varchar(20));".format(table_name))
        print('Table has been created successfully')
        conn.commit()  # permanently store all the transaction on the server

    elif choice == 3:
        uid = int(input('Enter user ID'))
        password = input('Enter password')
        cursor.execute("Insert MyTable(UserID, Password) VALUES (?,?)", (uid, password))
        print('Record has been inserted successfully')
        conn.commit()

    elif choice == 4:
        table_name = input('Enter table name')
        cursor.execute("select * from {};".format(table_name))
        result = cursor.fetchall()
        # print(type((result)))
        for x in result:
            print(x)
        # print(type(x)) # row datatype
        conn.commit()

    elif choice == 5:
        uid = int(input('Enter user ID'))
        cursor.execute("delete MyTable where UserID = ?", uid)
        print('Record has been deleted successfully')
        conn.commit()

    elif choice == 6:
        table_name = input('Enter table name')
        cursor.execute("delete {};".format(table_name))
        print('All record has been deleted successfully')
        conn.commit()

    elif choice == 7:
        table_name = input('Enter table name')
        cursor.execute("drop table {};".format(table_name))
        print('Table has been drop successfully')
        conn.commit()  # permanently store all the transaction on the server

    elif choice == 8:
        db_name = input('Enter database name to drop')
        cursor.execute("drop database {};".format(db_name))
        print('Database has been drop successfully')
        conn.commit()  # permanently store all the transaction on the server

    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()