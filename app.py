from flask import Flask. render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite://inventory.db'
db = SQLAchemy(app)


class Product(db.Model):

  __tablename__ = 'products'
  product_id    = db.Column(db.string(200), primary_key=True)
  date_created  = db.Column(db.DataTime, default=datetime.utcnow)

def __repr__(self):
  return '<product %r>' % self.product_id

Class Location(db.model):
    __Tablename__ = 'locations'
location-id       = db.Column(db.String(200), primary_key=True)
date_created      = db.column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
  retrun '<Location %r>' % self.location_id



