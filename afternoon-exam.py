import pyodbc
import numpy as np
import matplotlib.pyplot as plt

# connect to sql server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                      'Database={yusry_phcdc};'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permenantly store all the transaction on the server
cursor = conn.cursor()

# update database using python program
sid = int(input('Enter student rollno to edit'))
update_maths = float(input('Change Maths mark to : '))
cursor.execute("update usas_student_mark set math = ? where std_rollno = ?;", update_maths, sid)
print('Record has been updated successfully')

# display graph using python
cursor.execute("SELECT std_rollno,math FROM usas_student_mark")
result = cursor.fetchall()

x = np.array([x[0] for x in result])
y = np.array([x[1] for x in result])

plt.bar(x, y, color="green", width=0.5)

plt.title("Maths Mark Bar Graph Report")
plt.xlabel("Student ID")
plt.ylabel("Maths Mark")

plt.show()


