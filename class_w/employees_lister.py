import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()



class List_e():
    def list(self):
        print("-"*50)
        print("INFORMATIONS ABOUT EMPLOYEES\nlist:")
        print("-"*50)
        time.sleep(2)
        print(" ")
        sql = "SELECT idemployees, employee_name, employee_last_name, employee_address, employee_sector FROM employees"
        mycursor.execute(sql)
        employees = mycursor.fetchall()
        for self.i in employees:
            print(self.i)
            print(" ")
        time.sleep(2)
        

