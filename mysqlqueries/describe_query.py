from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="db1",
    ) as connection: 	
        show_table_query = "DESCRIBE "+input("Enter table: ")
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)
