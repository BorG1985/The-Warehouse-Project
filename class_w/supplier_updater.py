import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Updater_supplier():
    def updater_s(self):
        print("-"*50)
        print("CHANGE SUPPLIER INFORMATIONS")
        print("-"*50)
        self.supplier_to_c=input("Enter supplier id: ")
        self.name = input("Change supplier name: ")
        self.location = input("Change supplier location: ")
        self.address = input("Change supplier address: ")

        sql_update_supplier = "UPDATE supplier SET supplier_name = %s, supplier_location = %s ,supplier_address = %s WHERE idsupplier = %s"
        values = (self.name,self.location,self.address,self.supplier_to_c)
        mycursor.execute(sql_update_supplier, values)
        mydb.commit()

        print(mycursor.rowcount,"record(s) affected.")
        print("Successfully updated supplier informations")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")
