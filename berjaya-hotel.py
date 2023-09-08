import pyodbc
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
# establish connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                      'Database={yusry_berjaya_hotel};'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permenantly store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor

backtomenu = 'y'
while backtomenu == 'y':

    print('--------------------------------------------------------')
    print("\n\t\t\t WELCOME TO Yusry Berjaya Hotel\n")
    print('--------------------------------------------------------')
    print('1--> Room Info')
    print('2--> Room Service(Menu Card)')
    print('3--> Booking')
    print('4--> Order menu')
    print('5--> Payment')
    print('6--> Generate report for payment information')
    print('7--> Visualization of customer bills')

    choice = int(input('Enter your choice'))


    if choice == 1:

        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t YUSRY BERJAYA HOTEL\n')
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

        print('Standard Non-AC')
        print('| Room No. \t | Room Facility, Price & Status')
        cursor.execute('SELECT * FROM room_info WHERE room_no BETWEEN 1 AND 5')
        result=cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t | ', i[2], '| MYR ', i[3], ' | ', i[4])

        print('Standard AC')
        print('| Room No. \t | Room Facility, Price & Status')
        cursor.execute('SELECT * FROM room_info WHERE room_no BETWEEN 6 AND 10')
        result = cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t | ', i[2], '| MYR ', i[3], ' | ', i[4])

        print('3 Bed Non-AC')
        print('| Room No. \t | Room Facility, Price & Status')
        cursor.execute('SELECT * FROM room_info WHERE room_no BETWEEN 11 AND 15')
        result = cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t | ', i[2], '| MYR ', i[3], ' | ', i[4])

        print('3 Bed AC')
        print('| Room No. \t | Room Facility, Price & Status')
        cursor.execute('SELECT * FROM room_info WHERE room_no BETWEEN 16 AND 20')
        result = cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t | ', i[2], '| MYR ', i[3], ' | ', i[4])


    elif choice == 2:

        print('Breakfast')
        print('| Order No. \t | Menu Description & Price')
        cursor.execute('SELECT * FROM restaurant_menu WHERE order_no BETWEEN 1 AND 5')
        result = cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t\t |', i[2], '| MYR ', i[3])

        print('Lunch')
        print('| Order No. \t | Menu Description & Price')
        cursor.execute('SELECT * FROM restaurant_menu WHERE order_no BETWEEN 6 AND 10')
        result = cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t\t |', i[2], '| MYR ', i[3])

        print('Dinner')
        print('| Order No. \t | Menu Description & Price')
        cursor.execute('SELECT * FROM restaurant_menu WHERE order_no BETWEEN 11 AND 15')
        result = cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t\t |', i[2], '| MYR ', i[3])

        print('Snack')
        print('| Order No. \t | Menu Description & Price')
        cursor.execute('SELECT * FROM restaurant_menu WHERE order_no BETWEEN 16 AND 20')
        result = cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t\t |', i[2], '| MYR ', i[3])


    elif choice == 3:

        login = input('Are you a new customer, enter y/n :')
        if login == 'y':
            c_ic_passport = input('Enter customer IC / Passport')
            c_name = input('Enter customer name')
            c_age = int(input('Enter customer age'))
            c_address = input('Enter customer address')
            c_postal = input('Enter customer postal code')
            c_email = input('Enter customer email')
            c_phone = input('Enter customer phone number')
            cursor.execute('INSERT customer_info(customer_ic_passport,customer_name,customer_age,customer_address,customer_postal_code,customer_email,customer_phone) VALUES (?,?,?,?,?,?,?)',c_ic_passport, c_name, c_age, c_address, c_postal, c_email, c_phone)
            print('Record inserted successfully')
            conn.commit()
        elif login == 'n':
            cid = int(input('Enter your existing customer id'))
            cursor.execute('Select customer_id from customer_info where customer_id = ?',cid)
            result = cursor.fetchall()
            if cid in result[0]:
                cin = input('Enter check in date & time(for example : 2022-6-28 04:30:00')
                cout = input('Enter check out date & time(for example : 2022-6-29 04:30:00')
                rno = int(input('Enter room number'))
                cursor.execute('SELECT room_no,room_status from room_info where room_no = ?',rno)
                result = cursor.fetchall()
                if 'Available' in result[0]:
                    cursor.execute('INSERT booking_info(customer_id,check_in,check_out,room_no) VALUES (?,?,?,?)',cid,cin,cout,rno)
                    print('Successfully booked room')
                    cursor.execute("UPDATE room_info SET room_status = 'Not Available' WHERE room_no = ?",rno)
                    print('Room status updated successfully')
                else:
                    print('Room is not available.Try with another room')
            else:
                print('You are not valid customer.Please try again.Thank you.')


    elif choice == 4:

        login = input('Are you a new customer, enter y/n :')
        if login == 'y':
            c_ic_passport = input('Enter customer IC / Passport')
            c_name = input('Enter customer name')
            c_age = int(input('Enter customer age'))
            c_address = input('Enter customer address')
            c_postal = input('Enter customer postal code')
            c_email = input('Enter customer email')
            c_phone = input('Enter customer phone number')
            cursor.execute('INSERT customer_info(customer_ic_passport,customer_name,customer_age,customer_address,customer_postal_code,customer_email,customer_phone) VALUES (?,?,?,?,?,?,?)',c_ic_passport, c_name, c_age, c_address, c_postal, c_email, c_phone)
            print('Record inserted successfully')
            conn.commit()
        elif login == 'n':
            cid = int(input('Enter your existing customer id'))
            cursor.execute('Select customer_id from customer_info where customer_id = ?', cid)
            result = cursor.fetchall()
            if cid in result[0]:
                ord_no = 1
                while (ord_no != 0):
                    ord_no = int(input('Enter order number to add or press 0 to exit: '))
                    cursor.execute('SELECT order_no,food_price from restaurant_menu where order_no = ?', ord_no)
                    result = cursor.fetchall()
                    try:
                        if ord_no in result[0]:
                            cursor.execute('SELECT food_price from restaurant_menu where order_no = ?', ord_no)
                            result = cursor.fetchall()
                            for x in result:
                                tprice = [float(x[0]) for x in result]
                                tprice_str = str(tprice)[1:-1]
                                t_price = float(tprice_str)
                                cursor.execute('INSERT restaurant_bill(customer_id,order_no,total_price) VALUES (?,?,?)',cid, ord_no, t_price )
                                print('Successfully Ordered')
                        elif ord_no == 0:
                            pass
                        else:
                            print('Menu order number is not available.Try with another menu')
                    except Exception:
                        print('You enter an invalid number. Try again.')
            else:
                print('You are not valid customer.Please try again.Thank you.')


    elif choice == 5:

        cid = int(input('Enter customer ID'))
        cursor.execute("SELECT * FROM booking_info where customer_id = ?", cid)
        result1 = cursor.fetchall()
        global add_day
        add_day = 0
        for x in result1:
            extend_day_ch = input('Do you want to extend the room booking y/n')
            if extend_day_ch == 'y' or extend_day_ch =='Y':
                add_day = int(input('Enter number of days to be extended'))
                cursor.execute("UPDATE booking_info SET additional_day=%d Where customer_id=%d"%(add_day,cid))
                print('Additional days successfully updated')
                conn.commit()

            print(" Payment")
            print(" --------------------------------")
            print("  MODE OF PAYMENT")

            print("  1- Cash")
            print("  2- Debit/Credit")
            print("  3- Online")


            room_no = [x[3] for x in result1]
            room_no_str = str(room_no)[1:-1]
            #print(room_no_str)

            cursor.execute("SELECT price_perday FROM room_info WHERE room_no = ?", room_no_str)
            result2 = cursor.fetchall()
            p_perday = [int(x[0]) for x in result2]
            p_perday_str = str(p_perday)[1:-1]
            p_perday_int = int(p_perday_str)

            cin = [x[1] for x in result1]
            cout = [x[2] for x in result1]
            cin_str = str(cin)[2:-2]
            cout_str = str(cout)[2:-2]
            ci = datetime.strptime(cin_str, '%Y-%m-%d')
            co = datetime.strptime(cout_str, '%Y-%m-%d')
            t_day = co - ci
            t_no_day = t_day.days

            cursor.execute("SELECT * FROM restaurant_bill where customer_id = ?", cid)
            result = cursor.fetchall()

            for y in result:
                sum = np.sum([y[2] for y in result])

            choice_pmode = int(input('Enter your choice for payment'))

            if choice_pmode == 1:
                customer_id = cid
                r_fee = sum
                total = np.add((p_perday_int * t_no_day), r_fee)
                total_str = str(total)
                pay_mode = 'Cash'
                pay_status = 'Paid'

                cursor.execute(
                    "Insert payment_info(customer_id,check_in,check_out,total_no_day,restaurant_fee,additional_day,total_price,payment_mode,payment_status) VALUES (?,?,?,?,?,?,?,?,?)",
                    (customer_id, cin_str, cout_str, t_no_day, r_fee, add_day, total_str, pay_mode, pay_status))
                cursor.execute("SELECT * FROM customer_info where customer_id = ?", cid)
                result4 = cursor.fetchall()
                c_name = ''.join([str(x[2]) for x in result4])

                cursor.execute("SELECT * FROM payment_info where customer_id = ?", cid)
                result3 = cursor.fetchall()
                checkin = [x[1] for x in result3]
                checkin_date = str(checkin)[2:-2]
                checkout = [x[2] for x in result3]
                checkout_date = str(checkout)[2:-2]
                cid = ''.join([str(x[0]) for x in result3])

                print("\n\n ---------------------------------------")
                print("           Yusry Berjaya Hotel")
                print(" ---------------------------------------")
                print("                  Bill")
                print(" ---------------------------------------")
                print(" Customer ID: ", cid)
                print(" Customer Name: ", c_name)
                print("\n Check-In: ", checkin_date, "\t\n Check-Out: ", checkout_date, "\t")
                print('Room price: ', p_perday_int)
                print('Number of day:', t_no_day)
                print('Additional day fee: ', add_day)
                print('Restaurant fee:', r_fee)
                r_service_amount = (t_no_day + add_day) * p_perday_int
                print('Room service fee: ', r_service_amount)
                total_amount = r_service_amount + r_fee
                print('Total bill: ', total_amount)
                print(" ---------------------------------------")
                cursor.execute("UPDATE payment_info SET total_price=? where customer_id=?", total_amount, cid)
                cursor.execute("UPDATE room_info SET room_status='Available' where room_no=?", room_no_str)
                print("          Thank You. Visit Again :)")
                print(" ---------------------------------------\n")
                conn.commit()
                break


            if choice_pmode == 2:
                customer_id = cid
                r_fee = sum
                total = np.add((p_perday_int * t_no_day), r_fee)
                total_str = str(total)
                pay_mode = 'Credit/Debit'
                pay_status = 'Paid'

                cursor.execute(
                    "Insert payment_info(customer_id,check_in,check_out,total_no_day,restaurant_fee,additional_day,total_price,payment_mode,payment_status) VALUES (?,?,?,?,?,?,?,?,?)",
                    (customer_id, cin_str, cout_str, t_no_day, r_fee, add_day, total_str, pay_mode, pay_status))
                cursor.execute("SELECT * FROM customer_info where customer_id = ?", cid)
                result4 = cursor.fetchall()
                c_name = ''.join([str(x[2]) for x in result4])

                cursor.execute("SELECT * FROM payment_info where customer_id = ?", cid)
                result3 = cursor.fetchall()
                checkin = [x[1] for x in result3]
                checkin_date = str(checkin)[2:-2]
                checkout = [x[2] for x in result3]
                checkout_date = str(checkout)[2:-2]
                cid = ''.join([str(x[0]) for x in result3])

                print("\n\n ---------------------------------------")
                print("           Yusry Berjaya Hotel")
                print(" ---------------------------------------")
                print("                  Bill")
                print(" ---------------------------------------")
                print(" Customer ID: ", cid)
                print(" Customer Name: ", c_name)
                print("\n Check-In: ", checkin_date, "\t\n Check-Out: ", checkout_date, "\t")
                print('Room price: ', p_perday_int)
                print('Number of day:', t_no_day)
                print('Additional day fee: ', add_day)
                print('Restaurant fee:', r_fee)
                r_service_amount = (t_no_day + add_day) * p_perday_int
                print('Room service fee: ', r_service_amount)
                total_amount = r_service_amount + r_fee
                print('Total bill: ', total_amount)
                print(" ---------------------------------------")
                cursor.execute("UPDATE payment_info SET total_price=? where customer_id=?", total_amount, cid)
                cursor.execute("UPDATE room_info SET room_status='Available' where room_no=?", room_no_str)
                print("          Thank You. Visit Again :)")
                print(" ---------------------------------------\n")
                conn.commit()
                break


            if choice_pmode == 3:
                customer_id = cid
                r_fee = sum
                total = np.add((p_perday_int * t_no_day), r_fee)
                total_str = str(total)
                pay_mode = 'Online'
                pay_status = 'Paid'

                cursor.execute("Insert payment_info(customer_id,check_in,check_out,total_no_day,restaurant_fee,additional_day,total_price,payment_mode,payment_status) VALUES (?,?,?,?,?,?,?,?,?)",(customer_id, cin_str, cout_str, t_no_day, r_fee, add_day, total_str, pay_mode, pay_status))
                cursor.execute("SELECT * FROM customer_info where customer_id = ?", cid)
                result4 = cursor.fetchall()
                c_name =''.join([str(x[2])for x in result4])

                cursor.execute("SELECT * FROM payment_info where customer_id = ?", cid)
                result3 = cursor.fetchall()
                checkin = [x[1] for x in result3]
                checkin_date = str(checkin)[2:-2]
                checkout = [x[2] for x in result3]
                checkout_date = str(checkout)[2:-2]
                cid =''.join([str(x[0])for x in result3])


                print("\n\n ---------------------------------------")
                print("           Yusry Berjaya Hotel")
                print(" ---------------------------------------")
                print("                  Bill")
                print(" ---------------------------------------")
                print(" Customer ID: ",cid )
                print(" Customer Name: ",c_name )
                print("\n Check-In: ", checkin_date, "\t\n Check-Out: ", checkout_date, "\t")
                print('Room price: ',p_perday_int)
                print('Number of day:',t_no_day)
                print('Additional day fee: ',add_day)
                print('Restaurant fee:',r_fee)
                r_service_amount= (t_no_day + add_day) * p_perday_int
                print('Room service fee: ',r_service_amount)
                total_amount = r_service_amount + r_fee
                print('Total bill: ',total_amount)
                print(" ---------------------------------------")
                cursor.execute("UPDATE payment_info SET total_price=? where customer_id=?",total_amount,cid)
                cursor.execute("UPDATE room_info SET room_status='Available' where room_no=?",room_no_str)
                print("          Thank You. Visit Again :)")
                print(" ---------------------------------------\n")
                conn.commit()
                break

            else:
                print('Invalid choice')

        else:
            print('Customer not available in booking record')

    elif choice == 6:
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t YUSRY BERJAYA HOTEL REPORT\n')
        print(
            '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

        print('| Customer ID \t | Check-in \t | Check-out \t  | Total number of day \t | Restaurant Fee \t | Additional Day \t | Total Bill \t | Payment_mode \t | Payment Status')
        cursor.execute('SELECT * FROM payment_info')
        result = cursor.fetchall()
        for i in result:
            print('|', i[0], '\t\t\t | ', i[1], '\t | ', i[2], '\t  | ', i[3], '\t\t\t\t\t\t | ', i[4], '\t\t\t | ', i[5], '\t\t\t\t | ', i[6], '\t\t | ', i[7], '\t\t\t | ', i[8])

    elif choice == 7:
        try:
            cursor.execute("SELECT customer_id,total_price FROM payment_info ")
            result = cursor.fetchall()

            x = np.array([x[0] for x in result])
            y = np.array([x[1] for x in result])

            plt.bar(x, y, color="red", width=0.3)

            plt.title("Customer Bills Bar Graph Report")
            plt.xlabel("ID of customer")
            plt.ylabel("Total bill (MYR)")

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















