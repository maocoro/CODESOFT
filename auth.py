from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g

from werkzeug.security import generate_password_hash, check_password_hash

from .models import User

from codesft import db

bp = Blueprint ('auth', __name__, url_prefix= '/auth')

@bp.route ('/register', methods = ('GET', 'POST'))
def register():

    if request.method == 'POST':
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        company = request.form.get('company')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get ('password')

        user = User (name,lastname,company,username, email, generate_password_hash(password))

        #validación de datos
        error = None

        #Comprobando nombre de usuario con los existentes
        user_email = user.query.filter_by(email = email).first()
        if user_email == None:
            db.session.add(user)
            db.session.commit()
            return redirect (url_for('auth.login'))
        else:
            error = f'el correo {email} ya esta registrado'
        
        flash(error)
        
    return render_template ('auth/register.html')

@bp.route ('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get ('password')

        #validación de datos
        error = None
        user = User.query.filter_by(email = email).first()

        if user == None or not check_password_hash(user.password, password):
            error = 'Correo o contraseña incorrecta'

        #Iniciando Sesión
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('code.post'))
        
        flash (error)
    return render_template ('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    User_id = session.get('user_id')

    if User_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(User_id)

@bp.route ('/logout')
def logout ():
    session.clear()
    return redirect (url_for('home.index'))

import functools
def login_requerired (view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect (url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


from werkzeug.utils import secure_filename
@bp.route('/profile/<int:id>', methods=('GET', 'POST'))
@login_requerired
def profile(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.username = request.form.get('username')
        password = request.form.get('password')

        error = None
        if len(password) != 0:
            user.password = generate_password_hash(password)
        elif len (password) > 0 and len (password) < 6:
            error = 'La contraseña debe tener mas de 6 caracteres'

        if request.files['photo']:
            photo = request.files ['photo']
            photo.save (f'codesft/static/media/{secure_filename(photo.filename)}')
            user.photo = f'media/{secure_filename(photo.filename)}'
        
        if error is not None:
            flash (error)
        else:
            db.session.commit()
            return redirect (url_for('auth.profile', id = user.id))
        
        flash (error)
    return render_template ('auth/profile.html', user = user)

