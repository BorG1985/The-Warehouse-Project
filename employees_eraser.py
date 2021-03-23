import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Eraser_e():
    def eraser(self):
        print("-"*50)
        print("ERASE EMPLOYEE INFORMATIONS")
        print("-"*50)
        self.employee_to_erase=input("Enter employee id: ")
        
        sql_erase_employee = "DELETE FROM employees WHERE idemployees = %s"
        values = (self.employee_to_erase,)
        mycursor.execute(sql_erase_employee, values)
        mydb.commit()

        print(mycursor.rowcount,"record(s) affected.")
        print("Successfully erased employee informations")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")