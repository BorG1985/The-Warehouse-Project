import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Eraser_supplier():
    def eraser_s(self):
        print("-"*50)
        print("ERASE SUPPLIER")
        print("-"*50)
        self.supplier_to_erase=input("Enter supplier id: ")
        
        sql_erase_supplier = "DELETE FROM supplier WHERE idsupplier = %s"
        values = (self.supplier_to_erase,)
        mycursor.execute(sql_erase_supplier, values)
        mydb.commit()

        print(mycursor.rowcount,"record(s) affected.")
        print("Successfully erased supplier informations")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")