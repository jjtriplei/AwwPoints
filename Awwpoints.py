from flask import Flask, render_template, request
from database import Manager
from models.user import User
from models.post import Post
from models import comment
import json
import testing

# Terminology:
# Controller
# My Main File

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/sign_up', methods=['POST', 'GET'])
def create_account():
    if request.method == 'POST':

        username = request.form["username"]
        email_address = request.form["emailAddress"]

        if User.get_user_by_username(username):
            print("True")
        else:
            print("False")

        return json.dumps({'success': True, "username_exists": False, "email_address_exists": False,
                           "password_incorrect": False}), 200, {'ContentType': 'application/json'}

    else:
        return render_template('sign_up.html')


@app.route('/credential_check', methods=['POST'])
def check_credentials():
    return 200


@app.route('/news')
def news():
    my_user = "JJTRIPLEI"
    some_array = [1, 15, 20, 25, 30, 35, 40]

    # This is using JINJA2 to render the index.html file and passing it the above
    # Variables.
    return render_template('index.html',
                           user=my_user,
                           some_numbers=some_array)

@app.route('/users')
def users():
    all_users = User.get_all_users()
    return render_template('users.html', all_users=all_users)


@app.route('/user/<int:user_id>')
def user(user_id):
    retrieved_user = User.get_user_by_user_id(user_id)
    return render_template('user.html', user_profile=retrieved_user)


# Only run this statement if someone directly runs this python file.
# If it's being imported - this will not run.
if __name__ == '__main__':
    Manager.check_tables_exist()
    app.run()
