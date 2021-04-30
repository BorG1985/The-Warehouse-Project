import mysql.connector,os,time
from class_w.employees_lister import List_e as List_e    # importovao sam classu iz filea koji radi listing uposlenih
from class_w.employees_inserter import Inserter_e as Inserter_e # importovao classu iz filea koji radi unos novog uposlenog
from class_w.employees_updater import Updater_e as Updater_e # importovao sam classu iz filea koji izmjenjuje podatke o uposlenom
from class_w.employees_eraser import Eraser_e as Eraser_e # importovao sam classu iz filea koji brise informacije o uposlenom

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()

class Employees_menu():
    def menu_e(self):
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

