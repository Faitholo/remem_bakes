from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import datetime

db = SQLAlchemy()


class Staff(db.Model):
    __tablename__ = 'staff'
     
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    sales = db.relationship('Sales', backref='sales', lazy=True)


class Sales(db.Model):
    __tablename__ = 'sales'
    
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    bread_type = db.Column(db.ARRAY(db.String(120)), nullable=False)
    bread_size = db.Column(db.String(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    

class Recipe(db.Model):
    __tablename__ = 'recipe'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    ingredients = db.Column(db.ARRAY(db.String(120)), nullable=False)

class Bread(db.Model):
    __tablename__ = 'bread'
    
    id = db.Column(db.Integer, primary_key=True)
    name = name = db.Column(db.String(60), nullable=False)
    bread_shape = db.Column(db.String(60), nullable=False)
    bread_type = db.Column(db.String(60), nullable=False)
    bread_size = db.Column(db.String(60), nullable=False)

