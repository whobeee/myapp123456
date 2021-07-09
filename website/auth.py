from flask import Blueprint, render_template, request, flash, redirect, url_for,Flask,jsonify

from .models import User,Data
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from . import website1
from .getConnectedHosts import getActiveHosts
from .sender import send_file





auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                
                login_user(user, remember=True)
                return redirect(url_for('auth.index'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
        return redirect(url_for('auth.index'))        

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        

        user = User.query.filter_by(email=email).first()
        
        new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        
        return redirect(url_for('auth.index'))

    return render_template('sign_up.html')

@auth.route('/index')
@login_required
def index():
    return render_template('index.html', segment='index')    


@auth.route('/table')
@login_required
def table1():
    alldata = Data.query.all()

    return render_template('table-basic.html',  Members = alldata )


@auth.route('table/insert',methods = ['POST'])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        name1 = request.form['name1']
        website = request.form['website']
        ipaddr = request.form['ipaddr']        

        my_data = Data(name=name, name1=name1 ,website=website ,ipaddr=ipaddr)

        

        db.session.add(my_data)

        db.session.commit()
        flash("Member Inserted Successfully")
        
        return redirect(url_for('auth.table1'))    

@auth.route('table/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.name1 = request.form['name1']
        my_data.website = request.form['website']
        my_data.ipaddr = request.form['ipaddr']

        db.session.commit()
        flash("Member Updated Successfully")

        return redirect(url_for('auth.table1'))




#This route is for deleting our employee
@auth.route('table/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Member Deleted Successfully")

    return redirect(url_for('auth.table1'))


@auth.route('/profile')
@login_required
def profile():
    

    return render_template('page-profile.html',  )

@auth.route('table/apply/<id>/', methods = ['GET', 'POST'])
@login_required
def apply(id):
    
    host = "192.168.1.7"
    
    alldata = Data.query.all()
    website1.block()
    send_file(host)
    return render_template('table-basic.html' ,Members = alldata )


@auth.route('table/netcut/<id>/', methods = ['GET', 'POST'])
@login_required
def netcut(id):
    alldata = Data.query.all()
    return render_template('table-basic.html', Members = alldata )     




@auth.route('table/hola')
@login_required
def summary():
	d = getActiveHosts()
	return jsonify(d)     





