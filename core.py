import sqlite3
import os
import getpass
from sqlite3 import Error
from prettytable import PrettyTable

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
     except Error as error:
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
    except Error as e:
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

def create_user():
     conn = connection(db)
     db_connect = conn.cursor()
     db_connect.execute("select count(*) from user")
     count = db_connect.fetchall()
     for val in count:
          user = val[0]
     if user == 0:
          print("Creating new user")
          uname = input("Enter Username: ")
          pword = getpass.getpass(prompt='Enter Password: ')
          data = (uname,pword)
          db_connect1 = conn.cursor()
          db_connect1.execute('insert into user (uname,password) values (?,?)', data)
          conn.commit()
          print("Thank you for creating account" )
          login()
     else:
          login()

def login():
     conn = connection(db)
     print("Enter login details")
     uname = input("Enter Username: ")
     pword = getpass.getpass(prompt='Enter Password: ')
     db_connect = conn.cursor()
     db_connect.execute('select password from user where uname=?',(uname,))
     db_pword = db_connect.fetchall()
     for n in db_pword:
          passwd = n[0]
     if passwd == pword:
          display()
     else:
          log = input("login failed...! Invalid user credentials.. Try again [y/n]")
          if log == 'y':
               login()
          else:
               exit()

#Frontend
def display():
     OPT = "Welcome to My Password Manager" + "\n" + \
     "1. Add an Entry" + "\n" + \
     "2. Search Entries" + "\n" + \
     "3. Edit Entries" + "\n" + \
     "4. Delete an Entry" + "\n" + \
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
          print("Thank you for using Password manager \n")
          exit()
     else:
          print("Invalid entry")
          display()

def insertion():
     print("Save your password")
     tag = input("Enter name for your entry: ")
     uname = input("Enter username: ")
     pword = getpass.getpass(prompt='Enter Password: ')
     data = (tag,uname,pword)
     conn = connection(db)
     handle = conn.cursor()
     handle.execute('insert into data (tag,uname,pswd) values (?,?,?)', data)
     conn.commit()
     display()



def search():
      val = input("Display all entries (y/n): ")
      if val == "y":
           display_all()
           tag = input("Enter the tag name: ")
      elif val == "n":
           tag = input("Enter the tag name: ")
      else:
           print("Invalid entry")
           display()
      conn = connection(db)
      handle = conn.cursor()
      handle.execute("select tag,uname,pswd from data where tag like ? ", ['%' + tag + '%'])
      records = handle.fetchall()
      t = PrettyTable(['Tag', 'Username', 'Password'])
      for row in records:
           t.add_row([row[0], row[1], row[2]])
      print(t)
      handle.close()
      display()

def display_all():
     conn = connection(db)
     handle = conn.cursor()
     handle.execute('select distinct tag from data')
     val = handle.fetchall()
     tmp = PrettyTable(['values'])
     for i in val:
          tmp.add_row([i[0]])
     print(tmp)
     handle.close()

def edit():
     conn = connection(db)
     handle = conn.cursor()
     sch = input("Enter the tag to edit: ")
     new_uname = input("Enter new Username: ")
     new_pword = input("Enter new Password: ")
     new_data = (new_uname,new_pword,sch)
     handle.execute('update data set uname = ?, pswd = ? where tag = ?',new_data)
     print("Record Updated Successfully" + "\n" + \
           "============================")
     handle.close()
     display()

def deletion():
     conn = connection(db)
     handle = conn.cursor()
     var = input("Enter the tag to delete: ")
     sql_query = """delete from data where tag=?"""
     handle.execute(sql_query,(var,))
     conn.commit()
     print("Record Deleted Successfully" + "\n" + \
           "============================")
     handle.close()
     display()

