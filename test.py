from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from the form
        username = request.form.get("username")
        password = request.form.get("password")

        # Logic check
        if username == "Jimmy" and password == "password":
            return "Success: Logged in!"
        else:
            # You could also use 'flash' messages here to show errors on the page
            return "Failure: Invalid credentials", 401 

    # If the method is GET, just show the form
    return render_template("forms.html")

if __name__ == "__main__":
    # 0.0.0.0 makes it accessible on your local network
    app.run(host="0.0.0.0", port=5000, debug=True)