
# E-Commerce Flask App

A simple full-stack e-commerce web application built with **Flask**, **SQLite**, and **HTML/CSS**. Users can browse products, add items to the cart, and view the cart total.

## Features
- Product listing page
- Add to cart using session storage
- Cart summary with subtotal and total
- SQLite database for storing products
- Clean starter structure for further enhancements

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML/CSS

## Project Structure
```text
.
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── cart.html
└── static/
```

## Run Locally
```bash
git clone <your-repo-url>
cd ecommerce-flask-app
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000)

## GitHub Description
Flask e-commerce app with product listing, cart functionality, and SQLite integration.

## LinkedIn Project Description
Developed a full-stack e-commerce web application using Flask and SQLite, implementing product browsing, cart management, and database integration.

## Future Enhancements
- User authentication
- Payment integration
- Order history
- Admin dashboard
