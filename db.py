import argparse
from os import path, environ
from dotenv import load_dotenv
from api.model.mysqlmanager import MySQLManager
from api.model.user.model import create_user_table, drop_user_table
from api.model.form.model import create_form_table, drop_form_table


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DB")


def create_table(tablename=None):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if not tablename:
            print("Creating User Table")
            print("***" * 10)
            if create_user_table(cur):
                print("User table created successfully")
            else:
                print("User table already exists")
            print("\n")
            print("Creating Form Table")
            print("***" * 10)
            if create_form_table(cur):
                print("Form table created successfully")
            else:
                print("Form table already exists")
        elif tablename == "user":
            print("Creating User Table")
            if create_user_table(cur):
                print("User table created successfully")
            else:
                print("User table already exists")
        elif tablename == "form":
            print("Creating Form Table")
            if create_form_table(cur):
                print("Form table created successfully")
            else:
                print("Form table already exists")


def drop_table(tablename=None):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if not tablename:
            print("Droping User Table")
            print("***" * 10)
            if drop_user_table(cur):
                print("User table deleted successfully")
            else:
                print("Error while droping User Table.\nMaybe Table doesn't exists.")
            print("\n")
            print("Droping Form Table")
            print("***" * 10)
            if drop_form_table(cur):
                print("Form table deleted successfully")
            else:
                print("Error while droping Form Table.\nMaybe Table doesn't exists.")
        elif tablename == "user":
            print("Droping User Table")
            if drop_user_table(cur):
                print("User table deleted successfully")
            else:
                print("Error while droping User Table.\nMaybe Table doesn't exists.")
        elif tablename == "form":
            print("Droping Form Table")
            if drop_form_table(cur):
                print("Form table deleted successfully")
            else:
                print("Error while deleting Form Table.\nMaybe Table doesn't exists.")


parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    "--table",
    dest="tablename",
    help="create Table. Note: value --all will create all necessary tables",
    type=str,
)
parser.add_argument(
    "-d",
    "--drop",
    dest="table",
    help="create Table. Note: value --all will create all necessary tables",
    type=str,
)
args = parser.parse_args()
droptable = args.table
createtable = args.tablename

if createtable:
    if createtable == "all":
        create_table()
    elif createtable.lower() == "user":
        create_table("user")
    elif createtable.lower() == "form":
        create_table("form")
    else:
        print("Trying to create invalid table")

if droptable:
    if droptable == "all":
        drop_table()
    elif droptable.lower() == "user":
        drop_table("user")
    elif droptable.lower() == "form":
        drop_table("form")
    else:
        print("Trying to drop invalid table")
