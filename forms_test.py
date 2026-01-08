from flask import Flask, render_template,request, Response,send_from_directory,jsonify
import os
import uuid
import pandas as pd
import json


app = Flask(__name__, template_folder= "templates")

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template("forms.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "Jimmy" and password == "password":
            return f"success to login"
        else:
            return f"failure to login"

#Here we are creating a custom function to create download directory and process the doenload file
@app.route("/download_function_csv_2", methods=["POST"])
def download_function():
    file = request.files.get("file")
    if not file:
        return "No file uploaded", 400

    # Read the Excel file
    df = pd.read_excel(file)

    # Ensure download directory exists
    download_folder = "downloads"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Generate unique filename
    filename = f"{uuid.uuid4()}.csv"
    file_path = os.path.join(download_folder, filename)
    
    # Save as CSV
    df.to_csv(file_path, index=False)

    # Redirect to the HTML page that holds the download link
    return render_template("download_page.html", filename=filename)

@app.route("/get_file/<filename>")
def get_file(filename):
    # as_attachment=True forces the browser to download the file
    return send_from_directory("downloads", filename, download_name="result.csv")


@app.route("/json_content")
def json_content():


  
if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)