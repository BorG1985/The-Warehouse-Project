import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Inserter_supplier():
    def inserter_s(self):
        print("-"*50)
        print("ENTER NEW SUPPLIER")
        print("-"*50)
        self.name = input("Enter supplier name: ")
        self.location = input("Enter supplier location: ")
        self.address = input("Enter supplier address: ")

        sql_enter_supplier = "INSERT INTO supplier (supplier_name,supplier_location,supplier_address) VALUES (%s,%s,%s)"
        values = (self.name,self.location,self.address)
        mycursor.execute(sql_enter_supplier, values)
        mydb.commit()

        print(mycursor.rowcount,"record inserted.")
        print("New supplier successfully added.")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")
