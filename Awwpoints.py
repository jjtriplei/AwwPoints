from flask import Flask, render_template, request
from database import Manager
from models.user import User
from models import post
from models import comment
import testing

# Terminology:
# Controller
# My Main File

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sign_up', methods=['POST', 'GET'])
def create_account():
    if request.method == 'POST':
        user.username = request.form["username"]
        user.email = request.form["email_address"]
        user.profile_pic = request.form["profile_pic"]
        print("Username = " + str(user.username))
        print("Email Address = " + str(user.email))
        print("YOU DID IT")
        return {'success': True}
    else:
        return render_template('sign_up.html')


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
