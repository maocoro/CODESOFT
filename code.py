from flask import Blueprint, request, flash, redirect, url_for, g, render_template
from .auth import login_requerired
from .models import Computer
from codesft import db
from sqlalchemy import or_

bp = Blueprint ('code', __name__, url_prefix= '/code')

def search_posts(query):
    posts = Computer.query.filter(
        or_(
            Computer.serial.ilike(f'%{query}%'),
            Computer.responsable.ilike(f'%{query}%'),
            Computer.empresa.ilike(f'%{query}%'),
            Computer.marca.ilike(f'%{query}%')
        )
    ).all()
    return posts

@bp.route ('/post', methods = ('GET', 'POST'))
@login_requerired
def post():
    posts = Computer.query.all()

    if request.method == 'POST':
        query = request.form.get('search')
        posts = search_posts(query)
        value = 'hidden'
        return render_template ('admin/posts.html', posts = posts, value = value)

    return render_template ('admin/posts.html', posts = posts)

@bp.route ('/create', methods = ('GET', 'POST'))
@login_requerired
def create():
    if request.method == 'POST':
        serial = request.form.get('serial')
        responsable = request.form.get('responsable')
        empresa = request.form.get('empresa')
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        procesador = request.form.get('procesador')
        ram = request.form.get('ram')
        almacenamiento = request.form.get('almacenamiento')
        descripcion = request.form.get('ckeditor')

        post = Computer(g.user.id, serial, responsable, empresa, marca, modelo, procesador, ram, almacenamiento, descripcion)

        error = None

        #Comporarando url de post con los existentes
        post_serial = Computer.query.filter_by(serial = serial).first()
        if post_serial == None:
            db.session.add(post)
            db.session.commit()
            flash(f'El computador {post.serial} se registro correctamente')
            return redirect(url_for('code.post'))
        else:
            error = f'El Serial {serial} ya está registrado'
        flash (error)
    return render_template ('admin/create.html')

@bp.route ('/update/<int:id>',methods = ('GET', 'POST'))
@login_requerired
def update(id):
    post = Computer.query.get_or_404(id)

    if request.method == 'POST':
        post.responsable = request.form.get('responsable')
        post.empresa = request.form.get('empresa')
        post.ram = request.form.get('ram')
        post.almacenamiento = request.form.get('almacenamiento')
        post.descripcion = request.form.get('ckeditor')

        db.session.commit()
        flash(f'El Equipo {post.serial} se ha actulizado correctamente')
        return redirect(url_for('code.post'))
    return render_template ('admin/update.html', post = post)

@bp.route('/delele/<int:id>')
@login_requerired
def delete(id):
    post = Computer.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash(f'El equipo {post.serial} se eliminó correctamente')

    return redirect(url_for('code.post'))