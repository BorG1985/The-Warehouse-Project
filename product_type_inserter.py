import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Inserter_product_type():
    def inserter_p_t(self):
        print("-"*50)
        print("ENTER NEW PRODUCT TYPE")
        print("-"*50)
        self.name = input("Enter product type: ")

        sql_enter_product_type = "INSERT INTO product_type (product_type_name) VALUES (%s)"
        values = (self.name,)
        mycursor.execute(sql_enter_product_type, values)
        mydb.commit()

        print(mycursor.rowcount,"record inserted.")
        print("New product type successfully added.")
        print(" ")
        print("return to the MAIN MENU")
        time.sleep(3)
        os.system("cls")