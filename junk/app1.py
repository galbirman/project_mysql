from datetime import datetime

from flask import Flask
    
app = Flask(__name__)

@app.route("/")
def home():    
    return "My first project"
    
@app.route("/<name>")              
def hello_name(name):              
    return "Hello "+ name  
    
@app.route("/time")
def time():
    date = datetime.now()
    return date.strftime("%d/%m/%y, %H:%M")
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
