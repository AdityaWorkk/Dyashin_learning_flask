from flask import Flask, render_template,request, Response,send_from_directory
import os
import uuid
import pandas as pd


app = Flask(__name__, template_folder= "templates")

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template("4_forms.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "Jimmy" and password == "password":
            return f"success to login"
        else:
            return f"failure to login"
        

#{#name is used for exact match in the flask file}


#File upload
@app.route("/file_upload", methods=["GET","POST"])
def file_upload():
    file = request.files.get("file")

    if file.content_type == "text/plain":
        return file.read().decode()
    elif file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or \
        file.content_type == "application/vnd.ms-excel":
        df = pd.read_excel(file)
        return df.to_html()


#Creating a response to allow client to download csv (Responding back)
@app.route("/convert_csv", methods=["POST"]) 
def convert_csv():
    file = request.files.get("file")
    
    if not file:
        return "No file uploaded", 400

    df = pd.read_excel(file)

    # Create the Response object
    return Response(
        #csv_data
        df.to_csv(index=False),
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=forms_result_csv.csv"
        }
    )


#Creating a custom download page(Like hoe we have in youtube_to_mp3 converters)

#Here we are creating a custom function to create download directory and process the doenload file
@app.route("/download_function_csv_2", methods=["POST"])
def download_function():
    file = request.files.get("file")
    if not file:
        return "No file uploaded", 400

    df = pd.read_excel(file)

    # Ensure download directory exists
    download_folder = "downloads"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Generate unique filename
    filename = f"{uuid.uuid4()}.csv"                       #To generate unique ID to not repeat the file name again
    file_path = os.path.join(download_folder, filename)    # Saves the file in excel format itself in the download folder

    df.to_csv(file_path, index=False)

    return render_template("5_download_page.html", filename=filename)

@app.route("/get_file/<filename>")
def get_file(filename):
    # as_attachment=True forces the browser to download the file
    return send_from_directory("downloads", filename, download_name="result.csv") 


  
if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)
