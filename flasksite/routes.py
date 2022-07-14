from flask import render_template, url_for, flash, redirect
# from flask_bcrypt import Bcrypt
from flasksite.forms import RegistrationForm, LoginForm
# from flask_behind_proxy import FlaskBehindProxy
# from flask_sqlalchemy import SQLAlchemy
from flasksite.model import User
from flasksite import app, bcrypt, db, proxied


@app.route("/home")
def home():
  return render_template('home.html', subtitle="Home", text="This is the home page")


@app.route("/about")
def second_page():
  return render_template('about.html', subtitle="About", text="This is the second page")


@app.route("/")
@app.route("/register", methods=['GET', 'POST'])
def register():
  login_form = LoginForm()
  reg_form = RegistrationForm()
  if reg_form.validate_on_submit():
    user = User(username=reg_form.username.data, email=reg_form.email.data, password_hash=hash_pass(reg_form.password.data))
    db.session.add(user)
    db.session.commit()
    flash(f'Account created for {reg_form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', login_form=login_form, register_form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  # query the database to see if the username is present;
  # if so check for matching hash
  # if no username present reprompt;
  login_form = LoginForm()
  reg_form = RegistrationForm()
  if login_form.validate_on_submit():
    given_user = login_form.existing_user.data
    given_pass = login_form.existing_pass.data
    user_obj = User.query.filter_by(username=given_user).first()

    if (user_obj and
        bcrypt.check_password_hash(user_obj.password_hash, given_pass)):
      flash(f'Successfully logged in as {login_form.existing_user.data}!', 'success')
      return redirect(url_for('home'))
    else:
      flash(f'Invalid username and/or password')      
  return render_template('register.html', title="Register", login_form=login_form, register_form=reg_form)
  

def hash_pass(password):
  pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
  return pw_hash

  