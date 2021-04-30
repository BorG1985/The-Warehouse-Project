import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Updater_product():
    def updater_p(self):
        print("-"*50)
        print("CHANGE PRODUCT INFORMATIONS")
        print("-"*50)
        self.product_to_c=input("Enter product id: ")
        self.name = input("Change product name: ")
        self.type = int(input("Change product type id: "))
        self.code = int(input("Change product code: "))
        self.quantity = int(input("Change product quantity: "))
        self.supplier = int(input("Change product supplier id: "))
        self.price = float(input("Change product price: "))

        sql_update_product = "UPDATE products SET product_name = %s, idproduct_type = %s ,product_code = %s ,product_quantity = %s ,idsupplier = %s,product_price = %s WHERE idproducts = %s"
        values = (self.name,self.type,self.code,self.quantity,self.supplier,self.price,self.product_to_c)
        mycursor.execute(sql_update_product, values)
        mydb.commit()

        print(mycursor.rowcount,"record(s) affected.")
        print("Successfully updated product informations")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")
