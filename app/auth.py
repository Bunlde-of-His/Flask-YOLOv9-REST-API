from flask import Blueprint, jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "admin": "password"
}

auth_bp = Blueprint('auth', __name__)


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@auth_bp.route('/login', methods=['POST'])
@auth.login_required
def login():
    return jsonify({"message": "Login successful"}), 200
