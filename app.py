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

@app-route('/locations/', methods=["POST", "GET"])
def viewLocation():
  if (request.method == "POST") and ('location_name' in request.form):
    location_name = request.form["location_name"]
    new_location = Location(location_id=location_name)

  try:
    db.session.add(new_location)
    db.session.commit()
    return redirect("/locations/")

  except:
    locations = Location.query.order_by(Location.date_created).all()
    return "Error occured"
else:
locations = Location.query.order_by(Location.date_created).all()
return render_template("locations.html", locations=locations)

@app.route('/products/', methods=["POST", "GET"])
def viewProduct():
  if (request.method == "POST") and ('product_name' in request.form):
  product_name = request.form["product_name"]
  new_product = Product(product_id=product_name)

  try:
  db.session.add(new_product)
  db.session.commit()
  return redirect ("/products/")

  except:
  products = Products.query.order_by(Product.date_createde).all()
  return "Error occured"
  else:
  products = products.query.order_by(Product.date_created).all()
  return render_template("products.html", products=products)

  @app.route("/update-product/<name>", methods=["POST", "GET"])
  def updateProduct(name):
  product = Product.query.get_or_404(name)
  old_product = product.product_id

  if request.method == "POST":
    product.product_id  = reuest.form['product_name']

try:
  db.session.commit()
  updateProductInMovemnets(old_products, request.form['product_name'])
  return redirect("/products/")

except:
  return "Error occured"
else:
  retuen render_template("update-product.html", product=product)

@app.route("/delete-product/<name>")
def deleteProduct(name):
  product_to_delete = Product.query.get_or_404(name)

try:
  db.session.delete(product_to_delete)
  db.session.commit()
  return redirect("/products/")
  except:
  return "Error occured"

@app.route("/update-location/<name>", methods=["POST", "GET"])
def updateLocation(name):
location = Location.query.get_or_404(name)
old_location = location.location_id

if reuest.method == "POST":
location.location_id = request.form['location_name']

try:
  db.session.commit()
updateLocationInMovements(
  old_location, request.form['location_name'])
return redirect("/locations/")

except:
      return "Error occured"
else:
return render_template("update-location.html", location=location)

@app.route("/delete-location/<id>")
def deleteLocation(id):
  location_to_delete = Location.query.get_or_404(id)

try:
  db.session.delete(location_to_delete)
  db.session.commit()
return redirect("/locations/")
except:
return "Error occured"

@app.route("/movements/", methods=["POST", ["GET"])
def viewMovement():
  if request.method == "POST" :
     product_id      = request.form["productID"]
     qty             = request.form["qty"]
     fromLocation    = request.form["fromLocation"]
     toLocation      = request.form["tolocation"]
     new_movement    = ProductMovement(
       product_id=product_id, qty=qty, from_location=fromlocation, to_location=toLocation)

try:
  db.session.add(new.movement)
  db.session.commit()
  return redirect("/movements/")

except:
  return "Error occured"
else:
  products  = Product.query.order_by(Product.date_created).all()
  locations = Location.query.order_by(Location.date_created).all()
  movs      = ProductMovement.query\
  .join()Product, ProductMovement.product_id == Product.product_id)\
  .add_columns(
    ProductMovement.movement_id
    ProductMovement.qty
    Product.product_id
    ProductMovement.from_location,
    ProductMovement.to_location,
    ProductMovement.movement_time)\
  .all()

  movements  = productMovement.query.order_by(
    ProductMovement.movement_time).all()
  return render_template("movements.html", movements=movs, products=products, locations=locations)

@app.route("/update-movement/<int:id>", methods=["POST", "GET"])
def updateMovement(id):

  movement  = ProductMovement.query.get_or_404(id)
  products  = Product.query.order_by(Product.date_created).all()
  locations = Location.query.order_by(Location.date_created).all()

if request.method == "POST":
  movement.product_id = request.form["productId"]
  movement.qty        = request.form["qty"]
  movement.from_location = request.form["fromLocation"]
  movement.to_location = request.form["toLocation"]

try:
  db.session.commit()
  return redirect("/movements/")

except:
  return "Error occured"
else:
  return render_template("update-movement.html", movement=movement)

@app.route("/delete-movement/<int:id>")
def deleteMovement(id):
  movement_to_delete = ProductMovement.query.get_or_404(id)

  try:
    db.session.delete(movement_to_delete)
    db.session.commit()
    return redirect ("/movements/")
  except:
    return "Error occured"

@app.route("/product-balance/", methods=["POST", "GET"])
def productBalanceReport():
  movs = ProductsBalanceReport():
      join(Product, ProductMovement.product_id == Products.product_id).\
      add_columns(
        Product.product_id,
        ProductMovement.qty,
        productMovement.from_location,
        ProductMovement.to_location,
        ProductMovement.movement_time).\
order_by(ProductMovement.product_id).\
order_by(ProductMovement.movement_id).\
all()
balanceDict = defaultdict(lambda: defaultdict(dict))
tempProduct = ''
for mov in movs:
  row = mov[0]
if(tempProduct == row.product_id):
  if(row.to_location and not "qty" in balancedDict[row.product_id][row.to_location]):
    balancedDict[row.product_id][row.to_location]["qty"] = 0
elif (row.from_location and not "qty" in balancedict[row.product_id][row.from_location]):
balancedDict[row.product_id][row.from_location]["qty"] = 0 
if (row.to_location and "qty" in balanceDict[row.product_id][row.to_location]):
 balancedDict[row.product_id][row.to_location]["qty"] += row.qty
if (row.from_location and "qty" in balanceDict[row.product_id][row.from_location]):
  balancedDict[row.product_id][row.from_location]["qty"] -= row.qty
  pass
else :
  tempProduct = row.product_id
  if(row.to_location and not row.from_location):
    if(balancedDict):
      balancedDict[row.product_id][row.to_location]["qty"] = row.qty
else:
    balancedDict[row.product_id][row.to_location]["qty"] = row.qty

return render_template("product-balance.html", movement=balanceDict)

    


