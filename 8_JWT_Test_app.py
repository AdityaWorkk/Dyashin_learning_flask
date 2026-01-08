from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'    #The Database we will be using(Can use any database)
app.config['JWT_SECRET_KEY'] = 'SECRET KEY'     #This is what we are sending at the ending of the JWT token signature
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Database Model 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def landing():
    return render_template('10_JWT_login.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data['password'], method='pbkdf2:sha256')
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "User already exists"}), 400
        
    new_user = User(username=data['username'], password=hashed_pw)
    db.session.add(new_user)     #Adding the registered user to the database
    db.session.commit()
    return jsonify({"msg": "Registered successfully"}), 201

@app.route('/login', methods=['POST'])    #At login we are creating the new JWT Token
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.username)   #Creates the JWT tokens which are serverless
        return jsonify(access_token=token), 200
    
    return jsonify({"msg": "Invalid credentials"}), 401



@app.route('/home')
def home_page():
    return render_template('11_JWT_Test_home.html')



if __name__ == "__main__":
    app.run(debug=True)


