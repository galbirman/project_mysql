from datetime import datetime
from flask import Flask
from getpass import getpass
from mysql.connector import connect, Error
import json
import sys 
import mysqlx

    

app = Flask(__name__)

@app.route("/")
def home():    
    return "My first project"
    
@app.route("/create", methods =['GET', 'POST'])              
def create(): 
    try:
        with open('/project/jsonfile') as f:
         data = json.load(f)

        print("hello")
        print(data)

        with connect(
            host=data["host"],
            user=data["user"],
            password=data["password"],
            database=data["database"],
        ) as connection: 	
            query = "create database db1"
            with connection.cursor() as cursor:
                cursor.execute(query)
               
                result = cursor.fetchall()
                for row in result:
                    print(row,file=sys.stderr)
    except Error as e:
        print(e)
        
    return "DONE!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
