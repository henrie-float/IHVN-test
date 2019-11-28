
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="henrie",
  database="MariaDB"
)
mycursor = mydb.cursor()
dept = mycursor.execute("SELECT dept_no FROM dept_emp where emp_no = 10003;")
mycursor.execute("SELECT first_name, last_name from employees where dept_no = ", str(dept))

myresult = mycursor.fetchall()

for x in myresult:
  print(x)