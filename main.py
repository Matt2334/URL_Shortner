import requests
import time
import urllib.parse
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

website = input("What is the name of the website? ").capitalize()
url = urllib.parse.quote(input("Please paste the link you would like to shorten: "))
short = requests.get(f"https://api.shrtco.de/v2/shorten?url={url}").json()
shortened = short['result']['full_short_link']
print(f"Your new link is: {short['result']['full_short_link']}")

def CreateDatabase(name):
    con = psycopg2.connect(user="USER")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    cursor = con.cursor()
    cursor.execute(f"CREATE DATABASE {name}")
    return name
def InsertData(name, url, shortened, website):
    connected = psycopg2.connect(database=name)
    connected.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    mouse = connected.cursor()
    mouse.execute("CREATE TABLE short(id BIGSERIAL NOT NULL PRIMARY KEY, "
                  "website_name VARCHAR(50) NOT NULL, old_link VARCHAR(100), shortened_link VARCHAR(30))")
    mouse.execute("INSERT INTO short(website_name, old_link, shortened_link)"
                  f"VALUES ('{website}', '{url}', '{shortened}')")
def DeleteDatabase(database_name):
    con = psycopg2.connect(user="USER")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    cursor = con.cursor()
    cursor.execute(f"DROP DATABASE {database_name}")

ask = input("To create a new database? Type create: ")
if ask == "create" or ask == "Create":
    name = input("What do you want the name of your database to be: ")
    CreateDatabase(name)
    time.sleep(5)
    InsertData(name, url, shortened, website)
else:
    delete = input("If you would like to delete a database\n***WARNING THIS ACTION IS PERMANENT***"
               "\nType delete: ")
    if delete == "delete" or delete == "Delete":
        data_name = input("What is the name of the database you wish to delete? ")
        DeleteDatabase(database_name=data_name)
