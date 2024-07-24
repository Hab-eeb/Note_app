from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from app import db
from app.models import User 

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method ='pbkdf2:sha256')
    new_user = User(username=data['username'], password = hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': "User created!"}), 201

@auth_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username = data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login failed!'}), 401
    login_user(user)
    return jsonify({'message': 'Logged in successfully!'}), 200

@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully!'}), 200



