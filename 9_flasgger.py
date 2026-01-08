from flask import Flask, jsonify, render_template, request
from flasgger import Swagger

app = Flask(__name__)
# Initialize Swagger
swagger = Swagger(app)

@app.route("/", methods=["POST"])
def index():
    """
    Login Interface
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: Jimmy
            password:
              type: string
              example: password
    responses:
      200:
        description: Login attempt result
        schema:
          type: object
          properties:
            status:
              type: string
            message:
              type: string
    """
 
    
    # Flasgger sends data as JSON, so we use get_json()
    data = request.get_json()
        
    # Check if data exists to avoid errors
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
        
    username = data.get("username")
    password = data.get("password")
    if username == "Jimmy" and password == "password":
        return jsonify({"status": "success", "message": "Successfully logged in"}), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid credentials"}), 401
    
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)