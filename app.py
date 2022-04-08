from datetime import datetime
from flask import Flask
from getpass import getpass
from mysql.connector import connect, Error
import json
import sys
import mysqlx

from tasks import rabbitmq_add


app = Flask(__name__)


@app.route("/")
def home():
    print("ok")
    return "My first project"

@app.route("/create", methods=['GET', 'POST'])
def create():
    rabbitmq_add.delay(2, 2)
    return "DONE!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
