import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Inserter_e():
    def inserter(self):
        print("-"*50)
        print("ENTER NEW EMPLOYEE")
        print("-"*50)
        self.name = input("Enter employee name: ")
        self.last_name = input("Enter employee last name: ")
        self.address = input("Enter employee address: ")
        self.sector = input("Enter employee sector: ")
        self.permisions = int(input("Enter employee permision\n1)SUPER USER\n2)Administrator\n3)User\n4)Saler\nEnter number of permision: "))
        self.username = input("Enter employee username: ")
        self.password = input("Enter employee password: ")

        sql_enter_employee = "INSERT INTO employees (employee_name,employee_last_name,employee_address,employee_sector,idpermisions,employee_username,employee_password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (self.name,self.last_name,self.address,self.sector,self.permisions,self.username,self.password)
        mycursor.execute(sql_enter_employee, values)
        mydb.commit()

        print(mycursor.rowcount,"record inserted.")
        print("New employee successfully added.")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")
