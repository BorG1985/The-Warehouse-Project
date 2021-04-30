import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Updater_e():
    def updater(self):
        print("-"*50)
        print("CHANGE EMPLOYEE INFORMATIONS")
        print("-"*50)
        self.employee_to_c=input("Enter employee id: ")
        self.name = input("Enter new employee name: ")
        self.last_name = input("Enter new employee last name: ")
        self.address = input("Enter new employee address: ")
        self.sector = input("Enter new employee sector: ")
        self.permisions = int(input("Enter new employee permision\n1)SUPER USER\n2)Administrator\n3)User\n4)Saler\nEnter number of permision: "))
        self.username = input("Enter new employee username: ")
        self.password = input("Enter new employee password: ")

        sql_update_employee = "UPDATE employees SET employee_name = %s ,employee_last_name = %s,employee_address = %s,employee_sector = %s,idpermisions = %s,employee_username = %s,employee_password = %s WHERE idemployees = %s"
        values = (self.name,self.last_name,self.address,self.sector,self.permisions,self.username,self.password,self.employee_to_c)
        mycursor.execute(sql_update_employee, values)
        mydb.commit()

        print(mycursor.rowcount,"record(s) affected.")
        print("Successfully updated employee informations")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")
