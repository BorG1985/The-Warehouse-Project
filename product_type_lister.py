import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()



class List_product_type():
    def list_p_t(self):
        print("-"*50)
        print("ALL PRODUCTS TYPES IN WAREHOUSE\nlist:")
        print("-"*50)
        time.sleep(2)
        print(" ")
        sql = "SELECT * FROM product_type"
        mycursor.execute(sql)
        products = mycursor.fetchall()
        for self.i in products:
            print(self.i)
            print(" ")
        time.sleep(2) 
