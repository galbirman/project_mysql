from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection: 	
        query = input("Enter query: ")
        with connection.cursor() as cursor:
            cursor.execute(query)
except Error as e:
    print(e)
    
    
    
    
    
    
  
