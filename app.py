import flask
import psycopg2
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from forms.profile_form import ProfileForm
from flask import Flask, render_template
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

con = psycopg2.connect(host='localhost', dbname='data', user='postgres', password='1234', port=5432)


@app.route('/')
def main_window():  # put application's code here
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return render_template('/')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass






if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run()
