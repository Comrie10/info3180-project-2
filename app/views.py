import os
from . import app, db, login_manager
from flask import render_template, request, jsonify, send_file, send_from_directory
from app.forms import Login, User_Name,SignUp, Profile
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required, logout_user



@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/login', methods=['POST','GET'])
def login():
    form=Login()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        #user = db.session.execute (db.select(UserProfile).filterby(username=username)).scalar() #change the table if necessary

        #if user is not None and check_password_hash(user.password,password):
            #flash ("Invaild username/password", 'error')

        #login_user(user)
        # flash ("Successfully logged in", success)
        #return redirect(url_for('dashboard'))
    return render_template('login.vue',form=form)

@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(UserProfile).filter_by(id=id)).scalar()

#@app.route('/dashboard')
#@login_required
#def dashboard():
    # for loop for dashboard
    #return render_template('dashboard.vue', matches=matches)

@app.route('/signup', methods=['POST'])
def Signup():
  form = SignUp()
  if form.validate_on_submit():
    email = form.email.data
    photo = form.photo.data
    first_name = form.first_name.data
    last_name = form.last_name.data
    date_of_birth = form.date_of_birth.data 
    Gender = form.gender.data
    password = form.password.data
    # Save the photo file
    if photo:
        photo_filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
    # Create a new user and add to the database
    new_user = UserProfile(email=email, password=generate_password_hash(password), photo=photo_filename)
    db.session.add(new_user)
    db.session.commit()
    flash("Successfully signed up", 'success')
    return redirect(url_for('dashboard'))
  return render_template('signup.vue', form=form)

@app.route('/profile')
@login_required
def profile():
    user = current_user
    return render_template('profile.vue', user=user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Your successfully logged out",'success')
    return redirect(url_for('login'))


@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404