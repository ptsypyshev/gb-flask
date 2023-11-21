from flask import Flask, redirect, render_template, request, url_for, make_response
from lesson03.models import db, User
from lesson03.forms import SignUpForm, LoginForm
from bcrypt import gensalt, checkpw, hashpw
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'secret'
csrf = CSRFProtect(app)
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.route('/')
def html_index():
    context = {
        'title': 'Main page',
    }
    return render_template('index.html', **context)

@app.route('/sign-up/', methods=['GET', 'POST'])
def sign_up():    
    context = {
        'title': 'Sign-up page',
    }
    
    form = SignUpForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        hashed_password = hash_pw(form.password.data.encode())
        fname = form.first_name.data
        lname = form.last_name.data
        user = User(email=email, password=hashed_password, first_name=fname, last_name=lname)
        db.session.add(user)
        db.session.commit()
        context['name'] = fname
        context['operation'] = 'signed up'
        return render_template('success.html', **context)
    return render_template('sign-up.html', form=form, **context)

@app.route('/sign-in/', methods=['GET', 'POST'])
def sign_in():    
    context = {
        'title': 'Sign-in page',
    }
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        user = User.query.filter(User.email==email).first()
        if not verify_pw(password, user.password):
            context['bad_req'] = "Bad username or/and password"
            return render_template('sign-in.html', form=form, **context), 400
        response = make_response(redirect(url_for('profile')))
        response.set_cookie('username', user.first_name)
        response.set_cookie('email', email)
        return response
    return render_template('sign-in.html', form=form, **context)

@app.route('/sign-out/')
def sign_out():
    response = make_response(redirect(url_for('sign_in')))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response

@app.route('/profile/')
def profile():

    context = {
        'title': 'Profile page',
        'name': request.cookies.get('username')
    }
    return render_template('profile.html', **context)

def hash_pw(password):
    return hashpw(password, gensalt())

def verify_pw(password, hashed_password):
    return checkpw(password.encode(), hashed_password)

if __name__ == '__main__':
    app.run()