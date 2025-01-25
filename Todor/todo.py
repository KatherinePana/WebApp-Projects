# Importando Blueprint
from flask import Blueprint, render_template, request, redirect, url_for, g

# Agregando validación
from todor.auth import login_required
from .models import Todo, User
from todor import db

# Creando instancia
bp = Blueprint('todo', __name__, url_prefix='/todo')

# Creando ruta y función
@bp.route('/list')
@login_required 
def index(): 
    todos = Todo.query.all()
    return render_template('todo/index.html', todos = todos)

# Acción para crear listas
@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(g.user.id, title, desc)

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')

def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo