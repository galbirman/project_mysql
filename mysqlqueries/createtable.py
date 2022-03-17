from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database=input("Which DB to connect to? : "),
    ) as connection: 	
        create_reviewers_table_query = """
        CREATE TABLE reviewers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
	)
	"""
	
        with connection.cursor() as cursor:
            cursor.execute(create_reviewers_table_query)
            connection.commit()
except Error as e:
    print(e)
    
    
    
    

