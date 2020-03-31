import sqlite3
import os

db= "database.db"

##checks if the database file exists
def db_exist():
     if os.path.exists(db):
          return True

##Creates database connection
def connection(db):
     try:
          conn = sqlite3.connect(db)
          return conn
     except ConnectionError as error:
          print(error)
     return None

##Creates table in database
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        db_conn = conn.cursor()
        db_conn.execute(create_table_sql)
    except ConnectionError as e:
        print(e)
##Initial step that is executed
def step1():
     if not os.path.exists(db):
          os.mknod(db)

     user_table = """CREATE TABLE `user` (
     `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     `uname` BLOB,
     `password` BLOB);"""

     data_table = """CREATE TABLE `data` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`tag`	BLOB NOT NULL,
	`uname`	BLOB,
	`pswd`	BLOB);"""
     conn = connection(db)
     if conn is not None:
          create_table(conn, user_table)
          create_table(conn, data_table)
     else:
          print("Error in database connection")

def login():
     print("login")

#Frontend
def display():
     OPT = "Welcome to My Password Manager" + "\n" + \
     "1. Save a Password" + "\n" + \
     "2. Search Password" + "\n" + \
     "3. Edit Password" + "\n" + \
     "4. Delete Password" + "\n" + \
     "5. Exit"
     print(OPT)
     VAL = input("Enter your option: ")
     if VAL == "1":
          insertion()
     elif VAL == "2":
          search()
     elif VAL == "3":
          edit()
     elif VAL == "4":
          deletion()
     elif VAL == "5":
          print("Thank you for using Password manager")
          exit()
     else:
          print("Invalid entry")

def insertion():
     print("Selected option is insertion")

def search():
     print("search")

def edit():
     print("edit")

def deletion():
     print("delete")






