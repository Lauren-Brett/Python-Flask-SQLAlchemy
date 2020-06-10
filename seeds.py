from app import db
from app.models import User, Task


Task.query.delete()
User.query.delete()


# -- matching the username in routes
user = User(username="Lauren")
db.session.add(user)
# user2 = ..
# ad.session.add( ..)

db.session.commit()


users = User.query.all()

task1 = Task(title='Plants', description="Water plants", done=True, user=user)
db.session.add(task1)
task2 = Task(title='Buy Milk', description="I need milk for my tea!", user=user)
db.session.add(task2)
task3 = Task(title='Clean Kitchen', description="Hoover and tidy", user=user)
db.session.add(task3)
db.session.commit()


tasks = Task.query.all()

print(tasks)