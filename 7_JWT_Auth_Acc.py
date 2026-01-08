from flask import Flask,jsonify, request,session, render_template
import jwt
import functools
import datetime
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,get_jwt_identity

app = Flask(__name__, template_folder="templates")

app.config["SECRET KEY"] = "SECRET KEY"      #This is used at end of the JWT token signature
jwt = JWTManager(app)

@app.route("/")
def index():
    return render_template("9_JWT_Auth_Acc.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "Password":
        access_token = create_access_token(identity=username)
        return jsonify(access_token = access_token), 200
    
    return jsonify({ "mess": "bad credentials"}), 401
    
@app.route("/verify_token")
@jwt_required()
def verify():
    current_user = get_jwt_identity()
    return jsonify(log_in_as = current_user, message="Permission granted"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug= True)


