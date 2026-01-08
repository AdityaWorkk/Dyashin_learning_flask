from flask import Flask, request # 'request' (singular) is a Flask tool for incoming data
import requests                  # 'requests' (plural) is for fetching external APIs

app = Flask(__name__)



@app.route("/")
def index():
    return "<h1> Welcome to the website</h1>"



# Fixed: function now accepts 'name' and uses f-string
@app.route("/greet/<name>")    #To pass in arguments to the function from the URL by using <variable name>
def greet(name):
    return f"Hello, {name}"



# Fixed: Individual brackets for each variable and math logic
@app.route("/add/<int:number_1>/<int:number_2>")      #the variables can also be type casted
def add(number_1, number_2):
    result = number_1 + number_2
    return f"{number_1} + {number_2} = {result}"




# Fixed: Corrected variable names and f-string
@app.route("/name_greeting")
def name_greeting():
    # .get() prevents the app from crashing if 'greet' or 'name' is missing in URL
    greeting = request.args.get("greet", "Hello")   #to
    name = request.args.get("name", "Guest") 
    return f"{greeting} {name}"


#http://127.0.0.1:5000/name_greeting?greet=namaste&name=bob
#http://192.168.2.87:5000/name_greeting?name=bob
#example used



#Using methods to allow only specific method access the api endpoint
@app.route("/greets/<name>", methods = ["GET","POST"])
def greets(name):
    if request.method == "GET":
        return f"Hello" 
    if request.method == "POST":
        return f"Hello, {name}"






if __name__ == "__main__":
    # Fixed: Standard port is 5000
    app.run(host="0.0.0.0", port=5000, debug=True)

