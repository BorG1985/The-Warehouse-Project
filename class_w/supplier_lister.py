import mysql.connector,os,time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()



class List_supplier():
    def list_s(self):
        print("-"*50)
        print("ALL WAREHOUSE SUPPLIERS\nlist:")
        print("-"*50)
        time.sleep(2)
        print(" ")
        sql = "SELECT * FROM supplier"
        mycursor.execute(sql)
        suppliers = mycursor.fetchall()
        for self.i in suppliers:
            print(self.i)
            print(" ")
        time.sleep(2) 
