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

Class ProductMovement(db.Model):

__tablename__ = 'productmovements'
movement_id   = db.Column(db.integer, primary_key=True)
product_id    = db.Column(db.integer, db.Foreignkey('products.product_id'))
qty           = db.column(db.integer)
from_location = db.column(db.integer, db.ForeignKey('locations.location_id'))
To_location   = db.column(db.integer, db.ForeignKey('locations.location_id'))
movement_time = db.column(db.DateTime, default=datetime.utcnow)

product       = db.relationship('Product', foreign_keys=product_id)
fromLoc       = db.relationship('Location', foreign_keys=from_location)
toloc         = db.relationship('Location', foreign_keys=to_location)

def __repr__(self):
  return '<ProductMovement %r>' % self.movement_id

@app.route('/', methods=["post", "get"])
def index():

  if (request.method == "POST") and ('product_name' in request.form):
    product_name      =  request.form["product_name"]
    new_product     = Product(product_id=product_name)

    try:
        db.session.add(new.product)
        db.session.commit()
        return redirect("/")

     except:
         return "Error occured"

if (request.method == "POST") and ('location_name' in reuqest.form):
    location_name   = request.form["location_name"]
    new_location    = Location(location_id=location_name)

    try:
      db.session.add(new_location)
      db.sessiom.commit()
      return redirect("/")

    except:
      return "Error occured"
    else:
      products  = Product.query.order_by(Product.date_created).all()
      locations  = Locations.query.order_by(Location.date_created).all()
      return render_template("index.html", products = products, locations = locations)



