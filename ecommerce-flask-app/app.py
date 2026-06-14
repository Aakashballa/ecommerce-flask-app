
from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'change-this-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)


def seed_products():
    if Product.query.count() == 0:
        sample = [
            Product(name='Laptop', price=59999, description='Powerful laptop for coding and work'),
            Product(name='Headphones', price=2499, description='Wireless headphones with clear sound'),
            Product(name='Keyboard', price=1499, description='Mechanical keyboard for developers'),
            Product(name='Mouse', price=899, description='Ergonomic mouse for daily use'),
        ]
        db.session.add_all(sample)
        db.session.commit()

@app.before_request
def create_tables_once():
    db.create_all()
    seed_products()
    session.setdefault('cart', {})

@app.route('/')
def home():
    products = Product.query.all()
    cart_count = sum(session.get('cart', {}).values())
    return render_template('index.html', products=products, cart_count=cart_count)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1
    session['cart'] = cart
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = Product.query.get(int(pid))
        if product:
            subtotal = product.price * qty
            total += subtotal
            items.append({'product': product, 'qty': qty, 'subtotal': subtotal})
    return render_template('cart.html', items=items, total=total)

@app.route('/clear')
def clear_cart():
    session['cart'] = {}
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
