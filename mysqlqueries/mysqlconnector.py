import mysql.connector
from mysql.connector import errorcode
try:
	db_connection = mysql.connector.connect(host='127.0.0.1',
	port=3306,
	user='root',
	password='123456',
	database='db')
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	db_connection.close()
