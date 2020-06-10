import os
basedir = os.path.abspath(os.path.dirname(__file__))

#-- using db sqlite, could you any db here eg postgres
class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
