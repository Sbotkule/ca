from flask import Flask. render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite://inventory.db'
db = SQLAchemy(app)


class Product(db.Model)

