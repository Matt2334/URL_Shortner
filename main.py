import requests
import urllib.parse
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

url = urllib.parse.quote(input("Please paste the link you would like to shorten: "))
short = requests.get(f"https://api.shrtco.de/v2/shorten?url={url}").json()
print(f"Your new link is: {short['result']['full_short_link']}")

def CreateDatabase():
    name = input("What do you want the name of your database to be: ")
    con = psycopg2.connect(user="USER")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    cursor = con.cursor()
    cursor.execute(f"CREATE DATABASE {name}")
    connected = psycopg2.connect(database=name, user="USER")
    mouse = connected.cursor()
    mouse.execute("CREATE TABLE short(id BIGSERIAL NOT NULL PRIMARY KEY, "
                    "website_name VARCHAR(50) NOT NULL, old_link VARCHAR(60), shortened_link VARCHAR(30))")
