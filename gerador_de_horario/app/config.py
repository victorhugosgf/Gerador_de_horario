import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:senha@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
