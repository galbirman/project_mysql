from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database=input("Which DB to connect to? : "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)
