from flask import Flask
from database import db
from models import User

#from app.routes.auth import bp as auth_bp
#from app.routes.users import bp as users_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#app.register_blueprint(auth_bp)
#app.register_blueprint(users_bp)

@app.route('/health')
def hello_world():
    return 'Healthy!'

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



def main():
    with app.app_context():
        db.create_all()
    app.run(debug=True)



if __name__ == '__main__':
    main()
