import mysql.connector,os,time
# Importovane classe vezane za uposlenike:
from class_w.employees_lister import List_e as List_e    # importovao sam classu iz filea koji radi listing uposlenih
from class_w.employees_inserter import Inserter_e as Inserter_e # importovao classu iz filea koji radi unos novog uposlenog
from class_w.employees_updater import Updater_e as Updater_e # importovao sam classu iz filea koji izmjenjuje podatke o uposlenom
from class_w.employees_eraser import Eraser_e as Eraser_e # importovao sam classu iz filea koji brise informacije o uposlenom

# Importovane classe vezane za artikle:
from class_w.products_inserter import Inserter_product as Inserter_product # importovao classu iz filea koji radi unos novog artikla
from class_w.products_lister import List_products as List_products # importovao sam classu iz filea koji radi listing artikala
from class_w.product_updater import Updater_product as Updater_product # importovao sam classu iz filea koji izmjenjuje podatke o artiklu
from class_w.product_eraser import Eraser_product as Eraser_product # importovao sam classu iz filea koji brise artikal iz baze
from class_w.product_type_lister import List_product_type as List_product_type # importovao sam classu koja lista tipove artikala
from class_w.product_type_inserter import Inserter_product_type as Inserter_product_type # classa koja unosi novi tip artikala

# Importovane classe vezane za dobavljače
from class_w.supplier_inserter import Inserter_supplier as Inserter_supplier # importovao sam classu koja radi unos novog dobavljača
from class_w.supplier_lister import List_supplier as List_supplier # importovao sam classu koja radi listanje svih dobavljača
from class_w.supplier_updater import Updater_supplier as Updater_supplier # importovao sam classu koja radi izmjenu informacija o dobavljaču
from class_w.supplier_eraser import Eraser_supplier as Eraser_supplier # Importovao sam classu koja briše dobavljača


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()
os.system("cls")
print("Welcome to THE WAREHOUSE system")
print("Please:")
username = input("Enter username: ")
password = input("Enter password: ")

sql_authentication = "SELECT * FROM employees WHERE employee_username = %s AND employee_password = %s"
values = (username, password)
mycursor.execute(sql_authentication,values)

account = mycursor.fetchall()

for i in account:
    employee_name = i[1]
    employee_last_name = i[2]
    employee_username = i[6]
    employee_password = i[7]
    idpermisions = i[5]

account = True

while account:
    if account:
        if username == employee_username and password == employee_password:
            time.sleep(2)
            print("-"*100)
            
            print("You are now logged in as",employee_name, employee_last_name)
            print("Welcome ",employee_name, employee_last_name)
            print("-"*100)
            print("OPTIONS MENU\n \n1)Employees\n \n2)Products\n \n3)Suppliers\n \n4)EXIT")
            print(" ")
            option = input("Enter number of option: ")

#########################################   EMPLOYEES FOR SU   ###############################################

        if option == "1" and idpermisions == 1:
            os.system("cls")
            print("EMPLOYEES MENU")
            time.sleep(2)
            print(" ")
            print("1)Enter new employee\n \n2)Change employee informations\n \n3)Erase employee informations\n \n4)List all employees")
            print(" ")
            option_emp=input("Enter number of option: ")
            if option_emp == "1":
                os.system("cls")
                time.sleep(2)

                e_insert=Inserter_e() # objekat nad klasom koji vrsi unos novog zaposlenog
                e_insert.inserter()
            
            elif option_emp == "2":
                os.system("cls")
                time.sleep(2)

                List_E=List_e() # objekat nad klasom koji vrsi listanje spiska svih uposlenih
                List_E.list()
                
                Update_E=Updater_e() # objekat nad klasom koji vrsi izmjenu informacija uposlenih
                Update_E.updater()

            elif option_emp =="3":
                os.system("cls")
                time.sleep(2)

                List_E=List_e() # objekat nad klasom koji vrsi listanje spiska svih uposlenih
                List_E.list()

                Eraser_E=Eraser_e() # objekat nad klasom koji vrsi brisanje uposlenka
                Eraser_E.eraser()
            
            elif option_emp =="4":
                os.system("cls")
                
                List_E=List_e() # objekat nad klasom koji vrsi listanje spiska svih uposlenih
                List_E.list()

#########################################   PRODUCTS FOR SU   ###############################################

        elif option == "2" and idpermisions == 1:
            os.system("cls")
            print("PODUCTS MENU")
            time.sleep(2)
            print(" ")
            print("1)Enter new product\n \n2)Enter new product type\n \n3)Change product informations\n \n4)Erase product\n \n5)List all products in warehouse")
            print(" ")
            option_products=input("Enter number of option: ")
            if option_products == "1":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

                List_PT=List_product_type()
                List_PT.list_p_t()

                Inserter_p=Inserter_product() # objekat nad klasom koji vrsi unos novog artikla
                Inserter_p.inserter_p()

            elif option_products == "2":
                os.system("cls")
                time.sleep(2)

                List_PT=List_product_type()
                List_PT.list_p_t()

                Inserter_PT=Inserter_product_type()
                Inserter_PT.inserter_p_t()

            elif option_products == "3":
                os.system("cls")
                time.sleep(2)

                List_P=List_products() # objekat nad klasom koji vrsi listanje spiska svih artikala u skladistu
                List_P.list_p() 

                Updater_P=Updater_product()  # objekat nad klasom koji vrsi izmjenu informacija o artiklu
                Updater_P.updater_p()

            elif option_products == "4":
                os.system("cls")
                time.sleep(2)

                List_P=List_products()
                List_P.list_p()

                Erser_P=Eraser_product() # objekat nad klasom koji vrsi brisanje artikla
                Erser_P.eraser_p()

            elif option_products == "5":
                os.system("cls")
                time.sleep(2)

                List_P=List_products() # objekat nad klasom koji vrsi listanje spiska svih artikala u skladistu
                List_P.list_p() 
#########################################   SUPPLIERS FOR SU   ###############################################

        elif option == "3" and idpermisions == 1:
            os.system("cls")
            print("SUPPLIERS MENU")
            time.sleep(2)
            print(" ")
            print("1)Enter new supplier\n \n2)Change supplier informations\n \n3)Erase supplier\n \n4)List all suppliers")
            print(" ")
            option_suppliers=input("Enter number of option: ")
            if option_suppliers == "1":
                os.system("cls")
                time.sleep(2)

                Inserter_S=Inserter_supplier()
                Inserter_S.inserter_s()
            
            elif option_suppliers == "2":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

                Updater_S=Updater_supplier()
                Updater_S.updater_s()

            elif option_suppliers == "3":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

                Erase_S=Eraser_supplier()
                Erase_S.eraser_s()

            elif option_suppliers == "4":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

#########################################   EMPLOYEES FOR ADMINISTRATOR   ###############################################

        elif option == "1" and idpermisions == 2:
            os.system("cls")
            print("EMPLOYEES MENU")
            time.sleep(2)
            print(" ")
            print("1)Enter new employee\n \n2)Change employee informations\n \n3)List all employees")
            print(" ")
            option_emp=input("Enter number of option: ")

            if option_emp == "1":
                os.system("cls")
                time.sleep(2)

                e_insert=Inserter_e() # objekat nad klasom koji vrsi unos novog zaposlenog
                e_insert.inserter()
            
            elif option_emp == "2":
                os.system("cls")
                time.sleep(2)

                List_E=List_e() # objekat nad klasom koji vrsi listanje spiska svih uposlenih
                List_E.list()
                
                Update_E=Updater_e() # objekat nad klasom koji vrsi izmjenu informacija uposlenih
                Update_E.updater()
            
            elif option_emp =="3":
                os.system("cls")
                
                List_E=List_e() # objekat nad klasom koji vrsi listanje spiska svih uposlenih
                List_E.list()
#########################################   PRODUCTS FOR ADMINISTRATOR   ###############################################

        elif option == "2" and idpermisions == 2:
            os.system("cls")
            print("PODUCTS MENU")
            time.sleep(2)
            print(" ")
            print("1)Enter new product\n \n2)Change product informations\n \n3)List all products in warehouse")
            print(" ")
            option_products=input("Enter number of option: ")
            if option_products == "1":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

                List_PT=List_product_type()
                List_PT.list_p_t()

                Inserter_p=Inserter_product() # objekat nad klasom koji vrsi unos novog artikla
                Inserter_p.inserter_p()

            elif option_products == "2":
                os.system("cls")
                time.sleep(2)

                List_P=List_products() # objekat nad klasom koji vrsi listanje spiska svih artikala u skladistu
                List_P.list_p() 

                Updater_P=Updater_product()  # objekat nad klasom koji vrsi izmjenu informacija o artiklu
                Updater_P.updater_p()

            elif option_products == "3":
                os.system("cls")
                time.sleep(2)

                List_P=List_products() # objekat nad klasom koji vrsi listanje spiska svih artikala u skladistu
                List_P.list_p()     

#########################################   SUPPLIERS FOR ADMINISTRATOR   ###############################################

        elif option == "3" and idpermisions == 2:
            os.system("cls")
            print("SUPPLIERS MENU")
            time.sleep(2)
            print(" ")
            print("1)Enter new supplier\n \n2)Change supplier informations\n \n3)List all suppliers")
            print(" ")
            option_suppliers=input("Enter number of option: ")
            if option_suppliers == "1":
                os.system("cls")
                time.sleep(2)

                Inserter_S=Inserter_supplier()
                Inserter_S.inserter_s()
            
            elif option_suppliers == "2":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

                Updater_S=Updater_supplier()
                Updater_S.updater_s()

            elif option_suppliers == "3":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

#########################################   EMPLOYEES FOR USER   ###############################################      
        
        elif option == "1" and idpermisions == 3:
            os.system("cls")
            print("EMPLOYEES MENU")
            time.sleep(2)
            print(" ")
            print("1)List all employees")
            print(" ")
            option_emp=input("Enter number of option: ")

            if option_emp =="1":
                os.system("cls")
                
                List_E=List_e() # objekat nad klasom koji vrsi listanje spiska svih uposlenih
                List_E.list()

#########################################   PRODUCTS FOR USER   ###############################################
        
        elif option == "2" and idpermisions == 3:
            os.system("cls")
            print("PODUCTS MENU")
            time.sleep(2)
            print(" ")
            print("1)List all products in warehouse")
            print(" ")
            option_products=input("Enter number of option: ")

            if option_products == "1":
                os.system("cls")
                time.sleep(2)

                List_P=List_products() # objekat nad klasom koji vrsi listanje spiska svih artikala u skladistu
                List_P.list_p() 

#########################################   SUPPLIERS FOR USER   ###############################################

        elif option == "3" and idpermisions == 3:
            os.system("cls")
            print("SUPPLIERS MENU")
            time.sleep(2)
            print(" ")
            print("1)List all suppliers")
            print(" ")
            option_suppliers=input("Enter number of option: ")
            
            if option_suppliers == "1":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

#########################################   EMPLOYEES FOR SALER   ###############################################

        elif option == "1" and idpermisions == 4:
            os.system("cls")
            print("SORRY, YOU NOT ALLOWED TO USE THIS SECTION OF THE WAREHOUSE SYSTEM")
            print("return to MAIN MENU")
            time.sleep(2)
            print(" ")

#########################################   PRODUCTS FOR USER   ###############################################

        elif option == "2" and idpermisions == 4:
            os.system("cls")
            print("PODUCTS MENU")
            time.sleep(2)
            print(" ")
            print("1)Enter new product\n \n2)Enter new product type\n \n3)Change product informations\n \n4)List all products in warehouse")
            print(" ")
            option_products=input("Enter number of option: ")
            if option_products == "1":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

                List_PT=List_product_type()
                List_PT.list_p_t()

                Inserter_p=Inserter_product() # objekat nad klasom koji vrsi unos novog artikla
                Inserter_p.inserter_p()

            elif option_products == "2":
                os.system("cls")
                time.sleep(2)

                List_PT=List_product_type()
                List_PT.list_p_t()

                Inserter_PT=Inserter_product_type()
                Inserter_PT.inserter_p_t()

            elif option_products == "3":
                os.system("cls")
                time.sleep(2)

                List_P=List_products() # objekat nad klasom koji vrsi listanje spiska svih artikala u skladistu
                List_P.list_p() 

                Updater_P=Updater_product()  # objekat nad klasom koji vrsi izmjenu informacija o artiklu
                Updater_P.updater_p()

            elif option_products == "4":
                os.system("cls")
                time.sleep(2)

                List_P=List_products() # objekat nad klasom koji vrsi listanje spiska svih artikala u skladistu
                List_P.list_p() 

#########################################   SUPPLIERS FOR SALER   ###############################################

        elif option == "3" and idpermisions == 4:
            os.system("cls")
            print("SUPPLIERS MENU")
            time.sleep(2)
            print(" ")
            print("1)List all suppliers")
            print(" ")
            option_suppliers=input("Enter number of option: ")
            
            if option_suppliers == "1":
                os.system("cls")
                time.sleep(2)

                List_S=List_supplier()
                List_S.list_s()

#########################################   EXIT FOR ALL   ###############################################                

        elif option == "4" and idpermisions == 1 or idpermisions == 2 or idpermisions == 3 or idpermisions == 4:
            print("EXITING THE WAREHOUSE SYSTEM...")
            time.sleep(1)
            print("Logging out...")
            time.sleep(2)
            os.system("cls")
            print("You are logged out.")
            time.sleep(2)
            break
        

    else:
        print("Username or password are incorrect!")