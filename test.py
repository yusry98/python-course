import pyodbc
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
# establish connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                      'Database={yusry_berjaya_hotel};'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permenantly store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor

#Create bars

cursor.execute("SELECT customer_id,total_price FROM payment_info ")
result = cursor.fetchall()

x = np.array([x[0] for x in result])
y = np.array([x[1] for x in result])



plt.bar(x,y,color="red",width=0.3)

plt.title("Customer Bills Bar Graph Report")
plt.xlabel("ID of customer")
plt.ylabel("Total bill (MYR)")


plt.show()

conn.commit()

fruits = ["Apple", "Mango", "Orange", "Guava", "Peach"]

for item in fruits:
    print(item)

name = input("Please enter your name :")
age = input("Please enter your age :")
print("Person's name is, {1} and his age is {2} ".format(name, age))