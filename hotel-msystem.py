
backtomenu = 'y'
while backtomenu == 'y':

    print("\n\t\t\t\t\t\t WELCOME TO Yusry Berjaya Hotel\n")
    print('1--> Room Info')
    print('2--> Room Service(Menu Card)')
    print('3--> Booking')
    print('4--> Payment')
    print('5--> Record')

    import pyodbc
    import numpy as np
    # establish connection
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                          'Database={yusry_berjaya_hotel};'
                          'Trusted_Connection=yes;')
    conn.autocommit = True  # permenantly store all the transaction on the server
    cursor = conn.cursor()  # initialization of the cursor

    choice = int(input('Enter your choice'))


    if choice == 1:
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t YUSRY BERJAYA HOTEL\n')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
        cursor.execute('Select room_no,room_type,room_facility,price_perday,room_status from room_info')
        result=cursor.fetchall()
        for i in result:
            print(i)



    elif choice == 2:
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t YUSRY BERJAYA HOTEL MENU\n')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
        cursor.execute('Select * from restaurant_menu')
        result = cursor.fetchall()
        for i in result:
            print(i)
        conn.commit()

    elif choice == 3:
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



    elif choice == 4:
        cus_ic = input('Enter customer IC number')
        cursor.execute("SELECT * FROM booking where cus_ic = ?", cus_ic)
        result = cursor.fetchall()
        for x in result:
            print(" Payment")
            print(" --------------------------------")
            print("  MODE OF PAYMENT")

            print("  1- Credit/Debit Card")
            print("  2- TouchNgoEwallet")
            print("  3- Using FPX")
            print("  4- Cash")
            room_price = [x[8] for x in result]
            cursor.execute("SELECT * FROM restaurant where c_ic = ?", cus_ic)
            result = cursor.fetchall()
            for y in result:
                menu = [y[1] for y in result]
                sum = np.sum([y[1] for y in result])
                print('Amount to pay: {} + {}'.format(room_price,sum))
                break
            choice_pmode = int(input('Enter your choice for payment'))

            if choice_pmode == 1:
                cic = cus_ic
                amount = np.add(room_price,sum)
                amount_str = str(amount)[1:-1]
                pay_mode = 'Credit/Debit Card'
                cursor.execute(
                    "Insert payment(cic,amount,pay_mode) VALUES (?,?,?)",
                    (cic,amount_str,pay_mode))
                print('THANK YOU. VISIT AGAIN')
                conn.commit()
                break

            if choice_pmode == 2:
                cic = cus_ic
                amount = np.add(room_price,sum)
                amount_str = str(amount)[1:-1]
                pay_mode = 'TouchNgoEwallet'
                cursor.execute(
                    "Insert payment(cic,amount,pay_mode) VALUES (?,?,?)",
                    (cic, amount_str, pay_mode))
                print('THANK YOU. VISIT AGAIN')
                conn.commit()
                break

            if choice_pmode == 3:
                cic = cus_ic
                amount = np.add(room_price,sum)
                amount_str = str(amount)[1:-1]
                pay_mode = 'Using FPX'
                cursor.execute(
                    "Insert payment(cic,amount,pay_mode) VALUES (?,?,?)",
                    (cic,amount_str,pay_mode))
                print('THANK YOU. VISIT AGAIN')
                conn.commit()
                break

            if choice_pmode == 4:
                cic = cus_ic
                amount = np.add(room_price,sum)
                amount_str = str(amount)[1:-1]
                pay_mode = 'Cash'
                cursor.execute(
                    "Insert payment(cic,amount,pay_mode) VALUES (?,?,?)",
                    (cic, amount_str, pay_mode))
                print('THANK YOU. VISIT AGAIN')
                conn.commit()
                break

            else:
                print('Invalid choice')

        else:
            print('Customer not available in booking record')



    else:
        print('Invalid choice')


    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()

























