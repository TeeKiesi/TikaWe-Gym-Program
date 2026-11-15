from werkzeug.security import check_password_hash, generate_password_hash
from . import db

def login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])
    if len(result) == 0:
        return None
    user_id, password_hash = result[0]
    if not check_password_hash(password_hash, password):
        return None
    return user_id

def register(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def get_username(user_id):
    sql = "SELECT username FROM users WHERE id = ?"
    result = db.query(sql, [user_id])
    if len(result) == 0:
        return None
    return result[0]["username"]