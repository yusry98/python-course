print('Lunch')
print('| Order No. \t | Menu Description \t\t\t | Menu Price')
cursor.execute('SELECT * FROM restaurant_menu WHERE order_no BETWEEN 6 AND 10')
result = cursor.fetchall()
for i in result:
    print('|',i[0],'\t\t\t |', i[2], '\t\t\t\t\t\t |', i[3])


import pyodbc
import numpy as np
# establish connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                      'Database={yusry_berjaya_hotel};'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permenantly store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor

login  = int(input('Are you a new customer, enter 1 :'))
if login == 1:
    c_ic_passport = input('Enter customer IC / Passport')
    c_name = input('Enter customer name')
    c_age = int(input('Enter customer age'))
    c_address = input('Enter customer address')
    c_postal = input('Enter customer postal code')
    c_email = input('Enter customer email')
    c_phone = input('Enter customer phone number')
    cursor.execute('INSERT customer_info(customer_ic_passport,customer_name,customer_age,customer_address,customer_postal_code,customer_email,customer_phone) VALUES (?,?,?,?,?,?,?)', c_ic_passport,c_name,c_age,c_address,c_postal,c_email,c_phone)
    print('Record inserted successfully')
    conn.commit()


cus_name = input('Enter customer name')
        cus_ic = input('Enter customer IC number')
        cus_phone = input('Enter customer phone number')
        cus_email = input('Enter customer email')
        check_in = input('Enter check in date')
        check_out = input('Enter check out date')

        print("----SELECT ROOM TYPE----")
        print('1--> Single')
        print('2--> Single Deluxe')
        print('3--> Double')
        print('4--> Double Deluxe')
        print(("\t\tPress 0 for Room Prices"))

        choice_room = int(input('Enter your choice'))

        if choice_room == 1:
            room_id = 'RH1'
            room_type = 'Single'
            room_price = 80.95
            cursor.execute(
                "Insert booking(cus_name,cus_ic,cus_phone,cus_email,check_in,check_out,room_id,room_type, room_price) VALUES (?,?,?,?,?,?,?,?,?)",
                (cus_name, cus_ic, cus_phone, cus_email, check_in, check_out, room_id, room_type, room_price))
            print('ROOM BOOKED SUCCESSFULLY')
            conn.commit()

        elif choice_room == 2:
            room_id = 'RH2'
            room_type = 'Single Deluxe'
            room_price = 99.95
            cursor.execute(
                "Insert booking(cus_name,cus_ic,cus_phone,cus_email,check_in,check_out,room_id,room_type, room_price) VALUES (?,?,?,?,?,?,?,?,?)",
                (cus_name, cus_ic, cus_phone, cus_email, check_in, check_out, room_id, room_type, room_price))
            print('ROOM BOOKED SUCCESSFULLY')
            conn.commit()

        elif choice_room == 3:
            room_id = 'RH3'
            room_type = 'Double'
            room_price = 149.95
            cursor.execute(
                "Insert booking(cus_name,cus_ic,cus_phone,cus_email,check_in,check_out,room_id,room_type, room_price) VALUES (?,?,?,?,?,?,?,?,?)",
                (cus_name, cus_ic, cus_phone, cus_email, check_in, check_out, room_id, room_type, room_price))
            print('ROOM BOOKED SUCCESSFULLY')
            conn.commit()

        elif choice_room == 4:
            room_id = 'RH4'
            room_type = 'Double Deluxe'
            room_price = 179.95
            cursor.execute(
                "Insert booking(cus_name,cus_ic,cus_phone,cus_email,check_in,check_out,room_id,room_type, room_price) VALUES (?,?,?,?,?,?,?,?,?)",
                (cus_name, cus_ic, cus_phone, cus_email, check_in, check_out, room_id, room_type, room_price))
            print('ROOM BOOKED SUCCESSFULLY')
            conn.commit()

        else:
            print('Invalid choice')






























