import sqlite3
import os
import sys
db= "database.db"

def db_exist():
     if os.path.exists(db):
          return True




def db_create():
     try:
          conn = sqlite3.connect(db)
          return conn
     except ConnectionError as error:
          print(error)
     return None

def step1():
     user_table = """CREATE TABLE `user` (
     `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     `uname` BLOB,
     `password` BLOB);"""

     data_table = """CREATE TABLE `data` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`tag`	BLOB NOT NULL,
	`uname`	BLOB,
	`pswd`	BLOB);"""



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






