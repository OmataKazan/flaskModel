#model.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.dirname(__file__) #作成しているmodel.pyを格納しているファイル

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir,'data.sqlite')
app.congig['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.model):
    __tablename__ = 'persons'

    id=db.Column(db.Integet,primary_key=True)
    name =db.Column(db.Texe)
    db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        retrun "id = {self.id} , name={self.name}, age={self.age}"