from flask import Flask

app = Flask(__name__)                    #Initiallizing the app and assigning the name to app     

@app.route('/')                          #website is redirected to the root directory("/"), "@" called as decorator
def index():
    return "<h1>Hello world</h1>"

if __name__ == "__main__":                
    app.run(host="0.0.0.0",port=5555, debug=True)  #Host = 0.0.0.0 means local host, Port is already default 5000



