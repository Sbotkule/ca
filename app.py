from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://inventory.db'
db = SQLAlchemy(app)


class Product(db.Model):

  __tablename__ = 'products'
  product_id    = db.Column(db.String(200), primary_key=True)
  date_created  = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
        return '<product %r>' % self.product_id

class Location(db.Model):
    __tablename__ = 'locations'
location_id       = db.Column(db.String(200), primary_key=True)
date_created      = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
        return '<Location %r>' % self.location_id

class ProductMovement(db.Model):

__tablename__ = 'productmovements'
movement_id   = db.Column(db.Integer, primary_key=True)
product_id    = db.Column(db.String(200), db.Foreignkey('products.product_id'))
qty           = db.Column(db.Integer)
from_location = db.Column(db.String(200), db.ForeignKey('locations.location_id'))
to_location   = db.Column(db.String(200), db.ForeignKey('locations.location_id'))
movement_time = db.Column(db.DateTime, default=datetime.utcnow)

product       = db.relationship('Product', foreign_keys=product_id)
fromLoc       = db.relationship('Location', foreign_keys=from_location)
toloc         = db.relationship('Location', foreign_keys=to_location)

def __repr__(self):
  return '<ProductMovement %r>' % self.movement_id

@app.route('/', methods=["POST", "GET"])
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

if (request.method == "POST") and ('location_name' in request.form):
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
      locations  = Location.query.order_by(Location.date_created).all()
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
      products = Product.query.order_by(Product.date_createde).all()
      return "Error occured"
  else:
    products = product.query.order_by(Product.date_created).all()
    return render_template("products.html", products=products)

  @app.route("/update-product/<name>", methods=["POST", "GET"])
  def updateProduct(name):
  product = Product.query.get_or_404(name)
  old_product = product.product_id

  if request.method == "POST":
    product.product_id  = request.form['product_name']

try:
  db.session.commit()
  updateProductInMovemnets(old_product, request.form['product_name'])
  return redirect("/products/")

except:
  return "Error occured"
else:
  return render_template("update-product.html", product=product)

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

if request.method == "POST":
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
  movs = ProductMovement.query\
  .join()Product, ProductMovement.product_id == Product.product_id)\
  .add_columns(
    ProductMovement.movement_id,
    ProductMovement.qty,
    Product.product_id,
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
  movs = ProductMovement.query.\
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

 @app.route("/movements/get-from-locations/", methods=["POST"])
def getLocations():
  product = request.from["productId"]
  location = request.form["location"]
  locationDict = defaultdict(lambda: defaultdict(dict))
  locations = ProductsMovement.query.\
      filter(ProductMovement.product_id == product).\
      filter(ProductMovement.to_location != '').\
  add_columns(ProductMovement.from_location, ProductMovement.to_location, ProductMovement.qty).\
  all()

for key, location in enumerate(location):
  if(locationDict[location.to_location] and locationDict[location.to_location]["qty"]):
    locationDict[location.to_location]["qty"] += location.qty
  else:
    locationDict[location.to_loaction]["qty"] = location.qty

return locationDict


@app.route("/dub-location/", methods=["POST", "GET"])
def getDuplicate():
  location = location.form["location"]
  locations = Location.query.\
    filter(Location.location_id == location).\
    all()
  print(locations)
  if locations:
    return {"output": False}
  else:
    return {"output": True}

@app.route("/dub-products/", methods=["POST", "GET"])
def getPDublicate():
  product_name = request.form["product_name"]
  products = Products.query.\
      filter(Product.product_id == product_name).\
  all()
  print(products)
  if products:
    return {"output": False}
  else:
    return {"output": True}

def updateLocationInMovements(oldLocation, newLocation):
  movement = ProductMovement.query.filter(ProductMovement.from_location == oldLocation).all()
  movement2 = ProductMovement.query.filter(ProductMovement.to_location == oldLocation).all()
  for mov in movement2:
    mov.to_location = newLocation
  for mov in movement:
    mov.from_location = newLocation

db.session.commit()

def updateProductInMovements(oldProduct, newProduct):
  movement = ProductMovement.query.filter(ProductMovement.product_id == oldProduct).all()
  for mov in movement:
    mov.product_id = newProduct

db.session.commit()

if __name__ == "__main__":
  app.run(debug=True)
  
