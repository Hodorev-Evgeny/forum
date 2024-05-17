import flask
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from forms.profile_form import ProfileForm
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_window():  # put application's code here
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass






if __name__ == '__main__':
    app.run()
