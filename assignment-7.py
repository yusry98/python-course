# D22P1
class employee_info:
    def read_emp(self):
        self.empid = 1
        self.empname = 'Muhammad Yusri'
        self.empage = 24

class employee_job_info:
    def read_job_info(self):
        self.jobname = 'Web Designer'
        self.jobsalary = 5000.00

class display_employee(employee_info,employee_job_info):
    def disp_emp(self):
        print('Employee ID: ',self.empid)
        print('Employee Name: ', self.empname)
        print('Employee Age: ', self.empage)
        print('Job Name: ', self.jobname)
        print('Job Salary: ', self.jobsalary)

obj = display_employee()
obj.read_emp()
obj.read_job_info()
obj.disp_emp()


# D22P2
class bank:
    def mybank(self):
        self.bank_name = 'Bank Kerjasama Rakyat Berhad'
class account(bank):
    def myaccount(self):
        self.account_no = 220201499131
        self.account_holder = 'Muhammad Yusri bin Zakaria'
        self.account_balance = 5600.59
class deposit(account):
    def mydeposit(self):
        self.depo = 200.0
        self.new_balance = self.account_balance + self.depo
        print('Balance after deposit: ',self.new_balance)
class withdraw(account):
    def mywithdraw(self):
        self.withdraw = 350.0
        self.new_balance = self.account_balance - self.withdraw
        print('Balance after withdraw: ',self.new_balance)

child1obj = deposit()
child1obj.mybank()
child1obj.myaccount()
child1obj.mydeposit()
child2obj = withdraw()
child2obj.mybank()
child2obj.myaccount()
child2obj.mywithdraw()





# D22P3
class father:
    def myfathername(self):
        self.fname = 'Zakaria'

class child1(father):
    def myname(self):
        self.cname = 'Dalila'
        self.age = 34
        self.dob = '13/08/1988'
        print('Name: ',self.cname,self.fname)
        print('Age:',self.age)
        print('Date Of Birth: ',self.dob)

class child2(father):
    def myname(self):
        self.cname = 'Helmi'
        self.age = 31
        self.dob = '08/04/1991'
        print('Name: ',self.cname,self.fname)
        print('Age: ',self.age)
        print('Date Of Birth: ',self.dob)


childobj1 = child1()
childobj1.myfathername()
childobj1.myname()
childobj2 = child2()
childobj2.myfathername()
childobj2.myname()


# D24P4

# Create PHCDC_DB database
import pyodbc
# establish connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server={DESKTOP-TUN57G6\SQLEXPRESS};'
                      'Database={YusryZa};'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permenantly store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Create database PHCDC_DB")
print('Database has been created successfully')

# Create Trainer table and insert trainers information
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Create table Trainer(TrainerID int primary key, TrainerName varchar(30), TrainerPhono varchar(14), TrainerAddress varchar(30))")
print('Table has been created successfully')
cursor.execute("Insert Trainer values(101, 'Farith Amer', '+6012-7445677','KL')")
cursor.execute("Insert Trainer values(102, 'Irfan Isa', '+6012-5447855','Perak')")
print('Record has been inserted successfully')

# Create Participant table and insert prticipant's information
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Create table Participant(ParticipantID int primary key, ParticipantName varchar(30), ParticipantAge int, P_Phono varchar(14), P_Address varchar(30))")
print('Table has been created successfully')
cursor.execute("Insert Participant values(101, 'Meiyarasan',22, '+6013-4855225','KL')")
cursor.execute("Insert Participant values(102, 'Yusry', 24, '+6019-7455663','Perak')")
cursor.execute("Insert Participant values(103, 'Hamizan', 24, '+6010-45871123','Kedah')")
cursor.execute("Insert Participant values(104, 'CT Wong', 33, '+6012-7412366','Selangor')")
cursor.execute("Insert Participant values(105, 'Nadiya', 23, '+6014-7485665','Perlis')")
print('Record has been inserted successfully')

# Create Paricipant mark table and insert records
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("Create table Mark(ParticipantID int primary key, Malay INT, English INT, Science INT, Maths INT, Total INT)")
print('Table has been created successfully')
cursor.execute("Insert Mark values(101, 70, 85, 65, 84, null)")
cursor.execute("Insert Mark values(102, 85, 74, 56, 71, null)")
cursor.execute("Insert Mark values(103, 82, 73, 66, 77, null)")
cursor.execute("Insert Mark values(104, 81, 94, 74, 68, null)")
cursor.execute("Insert Mark values(105, 93, 85, 72, 75, null)")
print('Record has been inserted successfully')

# To generate report for all the trainer's information
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
print('| Trainer ID \t | Trainer Name \t | Traine Phone \t  | Trainer Address')
cursor.execute('SELECT * FROM Trainer')
result = cursor.fetchall()
for i in result:
        print('|', i[0], '\t\t\t | ', i[1], '  \t | ', i[2], '\t  | ', i[3])

# To generate report for all the participant's information
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
print('| Participant ID \t | Participant Name \t | Participant Age \t  | Participant Phone \t  | Participant Address')
cursor.execute('SELECT * FROM Participant')
result = cursor.fetchall()
for i in result:
        print('|', i[0], '  \t\t\t | ', i[1], '   \t\t\t | ', i[2], '  \t\t\t  | ', i[3], '\t\t  | ', i[4])

# To update total marks of the all participant's
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("UPDATE Mark SET Total = Malay+English+Science+Maths")
print('Total marks updated successfully')

# To generate report for participant whose attend the entire exam
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
print('| Participant ID \t | Participant Name')
cursor.execute('SELECT Mark.ParticipantID,ParticipantName FROM Mark left join Participant on Participant.ParticipantID = Mark.ParticipantID')
result = cursor.fetchall()
for i in result:
        print('|', i[0], '  \t\t\t | ', i[1])

# To delete the participant whose name is 'XXXXX'
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
cursor.execute("delete Participant where ParticipantID = 101")
print('Record has been deleted successfully')

# To generate participant's mark list report
import pyodbc
# establish
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TUN57G6\SQLEXPRESS;'
                      'Database=PHCDC_DB;'
                      'Trusted_Connection=yes;')
conn.autocommit = True  # permanently store all the transaction on the server
cursor = conn.cursor()  # initialization of the cursor
print('| Participant ID \t | Malay \t | English \t  | Science \t  | Maths \t\t  | Total')
cursor.execute('SELECT * FROM Mark')
result = cursor.fetchall()
for i in result:
        print('|', i[0], '  \t\t\t | ', i[1], '\t\t | ', i[2], '\t\t  | ', i[3], '\t\t  | ', i[4], '\t\t  | ', i[5])


