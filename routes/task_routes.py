from flask import Blueprint, render_template, flash, redirect, request, url_for
from database.engine import db
from database.models import Task


tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def get_all_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', my_tasks=tasks)


@tasks_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        flash('Задача добавлена!')
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')
        

@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task_detail.html', my_tasks=task)


@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted')
    return redirect(url_for('tasks.get_all_tasks'))


@tasks_bp.route('/update_status/<int:task_id>', methods=['POST'])
def update_status(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = 'Завершено'
    db.session.commit()
    flash('Status has been updated')
    return redirect(url_for('tasks.get_all_tasks'))