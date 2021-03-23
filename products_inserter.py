import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Inserter_product():
    def inserter_p(self):
        print("-"*50)
        print("ENTER NEW PRODUCT")
        print("-"*50)
        self.name = input("Enter product name: ")
        self.type = int(input("Enter product type id: "))
        self.code = int(input("Enter product code: "))
        self.quantity = int(input("Enter product quantity: "))
        self.supplier = int(input("Enter product supplier id: "))
        self.price = float(input("Enter product price: "))

        sql_enter_product = "INSERT INTO products (product_name,idproduct_type,product_code,product_quantity,idsupplier,product_price) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (self.name,self.type,self.code,self.quantity,self.supplier,self.price)
        mycursor.execute(sql_enter_product, values)
        mydb.commit()

        print(mycursor.rowcount,"record inserted.")
        print("New product successfully added.")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")