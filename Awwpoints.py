from flask import Flask, render_template, request
from database import tables, Manager
from models.user import User
from models import post
import testing

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/news')
def news():
    my_user = "JJTRIPLEI"
    some_array = [1, 15, 20, 25, 30, 35, 40]

    # This is using JINJA2 to render the index.html file and passing it the above
    # Variables.
    return render_template('index.html',
                           user=my_user,
                           some_numbers=some_array)

@app.route('/test')
def testingJinja():
    Joe_dic = tables.user_joe()
    return render_template('test.html', dictionary=Joe_dic)


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
    app.run()


