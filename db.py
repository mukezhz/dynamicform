import argparse
from os import path, environ
from dotenv import load_dotenv
from api.model.mysqlmanager import MySQLManager
from api.model.user.model import create_user_table, drop_user_table
from api.model.form.model import create_form_table, drop_form_table
from api.model.block.model import create_block_table, drop_block_table
from api.model.merge.userform import create_user_form_table, drop_user_form_table
from api.model.merge.formblock import create_form_block_table, drop_form_block_table


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
            if create_user_table(conn, cur):
                print("User table created successfully")
            else:
                print("User table already exists or Error has been occurred!")
            print("\n")
            print("Creating Form Table")
            print("***" * 10)
            if create_form_table(conn, cur):
                print("Form table created successfully")
            else:
                print("Form table already exists or Error has been occurred!")
            print("\n")
            print("Creating Block Table")
            print("***" * 10)
            if create_block_table(conn, cur):
                print("Block table created successfully")
            else:
                print("Block table already exists or Error has been occurred!")
            print("\n")
            print("Creating UserForm Table")
            print("***" * 10)
            if create_user_form_table(conn, cur):
                print("UserForm table created successfully")
            else:
                print("UserForm table already exists or Error has been occurred!")
            print("Creating FormBlock Table")
            print("***" * 10)
            if create_form_block_table(conn, cur):
                print("FormBlock table created successfully")
            else:
                print("FormBlock table already exists or Error has been occurred!")
        elif tablename == "user":
            print("Creating User Table")
            if create_user_table(conn, cur):
                print("User table created successfully")
            else:
                print("User table already exists or Error has been occurred!")
        elif tablename == "form":
            print("Creating Form Table")
            if create_form_table(conn, cur):
                print("Form table created successfully")
            else:
                print("Form table already exists or Error has been occurred!")
        elif tablename == "block":
            print("Creating Block Table")
            if create_block_table(conn, cur):
                print("Block table created successfully")
            else:
                print("Block table already exists or Error has been occurred!")
        elif tablename == "userform":
            print("Creating UserForm Table")
            if create_user_form_table(conn, cur):
                print("UserForm table created successfully")
            else:
                print("UserForm table already exists or Error has been occurred!")
        elif tablename == "formblock":
            print("Creating FormBlock Table")
            if create_form_block_table(conn, cur):
                print("FormBlock table created successfully")
            else:
                print("FormBlock table already exists or Error has been occurred!")


def drop_table(tablename=None):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if not tablename:
            print("Droping UserForm Table")
            print("***" * 10)
            if drop_user_form_table(conn, cur):
                print("UserForm table deleted successfully")
            else:
                print(
                    "Error while droping UserForm Table.\nMaybe Table doesn't exists."
                )
            print("Droping FormBlock Table")
            print("***" * 10)
            if drop_form_block_table(conn, cur):
                print("FormBlock table deleted successfully")
            else:
                print(
                    "Error while droping FormBlock Table.\nMaybe Table doesn't exists."
                )
            print("Droping User Table")
            print("***" * 10)
            if drop_user_table(conn, cur):
                print("User table deleted successfully")
            else:
                print("Error while droping User Table.\nMaybe Table doesn't exists.")
            print("\n")
            print("Droping Form Table")
            print("***" * 10)
            if drop_form_table(conn, cur):
                print("Form table deleted successfully")
            else:
                print("Error while droping Form Table.\nMaybe Table doesn't exists.")
            print("Droping Block Table")
            print("***" * 10)
            if drop_block_table(conn, cur):
                print("Block table deleted successfully")
            else:
                print("Error while droping Block Table.\nMaybe Table doesn't exists.")
        elif tablename == "user":
            print("Droping User Table")
            if drop_user_table(conn, cur):
                print("User table deleted successfully")
            else:
                print("Error while droping User Table.\nMaybe Table doesn't exists.")
        elif tablename == "form":
            print("Droping Form Table")
            if drop_form_table(conn, cur):
                print("Form table deleted successfully")
            else:
                print("Error while deleting Form Table.\nMaybe Table doesn't exists.")
        elif tablename == "block":
            print("Droping Block Table")
            if drop_block_table(conn, cur):
                print("Block table deleted successfully")
            else:
                print("Error while deleting Block Table.\nMaybe Table doesn't exists.")
        elif tablename == "userform":
            print("Droping UserForm Table")
            if drop_user_form_table(conn, cur):
                print("UserForm table deleted successfully")
            else:
                print(
                    "Error while deleting UserForm Table.\nMaybe Table doesn't exists."
                )
        elif tablename == "formblock":
            print("Droping FormBlock Table")
            if drop_form_block_table(conn, cur):
                print("FormBlock table deleted successfully")
            else:
                print(
                    "Error while deleting FormBlock Table.\nMaybe Table doesn't exists."
                )


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
    elif createtable.lower() == "block":
        create_table("block")
    elif createtable.lower() == "userform":
        create_table("userform")
    elif createtable.lower() == "formblock":
        create_table("formblock")
    else:
        print("Trying to create invalid table")

if droptable:
    if droptable == "all":
        drop_table()
    elif droptable.lower() == "user":
        drop_table("user")
    elif droptable.lower() == "form":
        drop_table("form")
    elif droptable.lower() == "block":
        drop_table("block")
    elif droptable.lower() == "userform":
        drop_table("userform")
    elif droptable.lower() == "formblock":
        drop_table("formblock")
    else:
        print("Trying to drop invalid table")
