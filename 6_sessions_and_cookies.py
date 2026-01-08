from flask import Flask,render_template,session

app = Flask(__name__,template_folder="templates")

app.secret_key = "SOME KEY" 


@app.route("/")
def index():
    return render_template("7_cookies_sessions.html", message="Index")

@app.route("/set_data")
def set_data():
    session["name"] = "Mike"                          #Creating session dictionary
    session["other"] = "hello world"
    return render_template("7_cookies_sessions.html", message = "session set")   #passing this message to the cookies html

@app.route("/get_data")
def get_data():
    if "name" in session.keys() and "others" in session.keys():
        name = session.get("name")                  #get the name from the "name" key of session
        other = session.get("other")
        return render_template("7_cookies_sessions.html", message=f"name: {name},other: {other}" )
    else:
        return render_template("7_cookies_sessions.html", message="No session found")
    
@app.route("clear_data")
def clear_data():
    session.clear()
    return render_template("7_cookies_sessions.html", message="Session cleared")




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

