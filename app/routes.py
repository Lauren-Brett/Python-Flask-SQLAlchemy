from app import app, db
from flask import render_template, request, redirect
from app.models import User, Task

@app.route('/<name>')
def index(name):
    return f"this is the route to your name: {name}"


@app.route('/')
def home():
    # -- in models we gave user the tasks - so we can get tasks through User
    user = User.query.get(1)
    tasks = user.tasks
    # -- tell it which file to render, and what
    return render_template("index.html",
                           title="Home", user=user, tasks=tasks)

@app.route('/tasks', methods=['POST'])
def create():
    user = User.query.get(1)
    # print(request.form)
    # return "Done"
    #-- taking 'name' field from html ie description
    task_title = request.form['title']
    task_desc = request.form['description']
    new_task = Task(title=task_title, description=task_desc, user=user)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

# -- diamonds are saying varible - converts string from url to this type
@app.route('/tasks/<int:task_id>', methods=['POST'])
def update(task_id):
    task = Task.query.get(task_id)
    task.done = True
    db.session.commit()
    return redirect("/")