from flask import Flask, render_template, request,Response
import pandas as pd
import io

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template("forms.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "Jimmy" and password == "password":
            return "success to login"
        else:
            return "failure to login"

@app.route("/file_upload", methods=["POST"])
def file_upload():
    # 1. Use the 'name' attribute from your HTML <input type="file" name="file">
    file = request.files.get("file")

    if not file:
        return "No file uploaded", 400

    # 2. Handle Plain Text
    if file.content_type == "text/plain":
        return file.read().decode("utf-8")

    # 3. Handle Excel (Spreadsheets)
    elif file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or \
         file.content_type == "application/vnd.ms-excel":
        df = pd.read_excel(file)
        return df.to_html()

    # 4. Handle Word Documents (Word docs are NOT dataframes)
    elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # Pandas cannot read Word docs. You would usually use 'python-docx' here.
        return "Word document received. (Note: Pandas cannot read Word files as DataFrames)."

    else:
        return f"File type {file.content_type} not supported for processing."
    

@app.route("/convert_csv", methods=["POST"])
def convert_csv():
    file = request.files.get("file")

    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype="text/csv"
        header = {
            "Content-Disposition": "Attachment": "filename= forms_result_csv.csv"
        }
    )
    return response



#=========================================================================================
@app.route("/download_function_csv_2", method=["POST"])
def download_function():
    
    file = request.files.get("file")

    df = pd.read_excel(file)

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    filename= f"{uuid.uuid4()}.csv"
    df.to_csv(os.path.join("downloads",filename))

    return render_template("download_page.html", filename=filename)


#We have to create the download page now and GET THE RESULT from DOWNLOAD FUNCTION CSV 2
@app.route("/download/<filename>")
def download_page(filename):
    return send_from_directory("downloads", filename,as_attachment= True, download_name="result.csv")


#===================================================================================================



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)




