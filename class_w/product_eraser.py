import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Eraser_product():
    def eraser_p(self):
        print("-"*50)
        print("ERASE PRODUCT")
        print("-"*50)
        self.product_to_erase=input("Enter product id: ")
        
        sql_erase_product = "DELETE FROM products WHERE idproducts = %s"
        values = (self.product_to_erase,)
        mycursor.execute(sql_erase_product, values)
        mydb.commit()

        print(mycursor.rowcount,"record(s) affected.")
        print("Successfully erased employee informations")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")
