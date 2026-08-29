from flask import Flask, request, session
from database import db
from models import User

#from app.routes.auth import bp as auth_bp
#from app.routes.users import bp as users_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "dev-secret-key-change-this-later"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#app.register_blueprint(auth_bp)
#app.register_blueprint(users_bp)

@app.route('/')
def hello_world():
    return 'Security Lab!'

# using the following route to initialize the database with some users for testing purposes

# @app.route("/init-users")
# def init_users():

#     if User.query.count() == 0:
#         users = [
#             User(
#                 username="alice",
#                 email="alice@example.com",
#                 password="alice123"
#             ),
#             User(
#                 username="bob",
#                 email="bob@example.com",
#                 password="bob123"
#             ),
#             User(
#                 username="charlie",
#                 email="charlie@example.com",
#                 password="charlie123"
#             )
#         ]

#         db.session.add_all(users)
#         db.session.commit()

#     return {
#         "message": "Users initialized",
#         "users": User.query.count()
#     }

# @app.route("/users")
# def users():

#     users = User.query.all()

#     return {
#         "users": [
#             {
#                 "id": user.id,
#                 "username": user.username,
#                 "email": user.email
#             }
#             for user in users
#         ]
#     }


# user login route
@app.route("/login", methods=["POST"])
def login():

    json_data = request.get_json()

    username = json_data.get("username")
    password = json_data.get("password")

    user = User.query.filter_by(username=username, password=password).first()

    if not user or user.password != password:
        return {"message": "Invalid username or password"}, 401

    session["user_id"] = user.id

    return {"message": "Login successful", "user_id": user.id}, 200


# user logout route
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return {"message": "Logout successful"}, 200


# user profile route
@app.route("/profile", methods=["GET"])
def profile():
    user_id = session.get("user_id")

    if not user_id:
        return {"message": "Authentication required"}, 401

    user = User.query.get(user_id)

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }, 200

# vulnerable route to demonstrate Insecure Direct Object Reference (IDOR) vulnerability
@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    
    user = User.query.get(user_id)  # vulnerable to IDOR, as it allows access to any user's data without proper authorization checks

    if not user:
        return {"message": "User not found"}, 404

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }, 200


# main function to run the app
def main():
    with app.app_context():
        db.create_all()
    app.run(debug=True)



if __name__ == '__main__':
    main()
