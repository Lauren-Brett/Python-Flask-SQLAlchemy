from app import db


#-- setting up two classes, 
# will create 2 tables with columns defined, 
# link tables, 
# lazy set so it will only bring back task when we ask for it
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # number of characters in string: 64
    username = db.Column(db.String(64), index=True)
    tasks = db.relationship("Task", backref="user", lazy="dynamic")


#-- overwrite
    def __repr__(self):
        return "<User {}>".format(self.username)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True)
    description = db.Column(db.Text())
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return "<Task {}".format(self.title)