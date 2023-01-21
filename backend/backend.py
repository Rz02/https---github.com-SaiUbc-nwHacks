from flask import Flask, render_template, request, jsonify
import functools
import csv
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['***'] = '***'
db = SQLAlchemy(app)


#Define Database with id, bus, stop and route
class User(db.Model):
    id = db.Column(db.Integer, primary_jey = True)
    bus = db.Column(db.Integer, unique = True, nullable = False)
    stop = db.Column(db.String(80), unique = True, nullable = False)
    route = db.Column(db.String(80), unique = True, nullable = False)
    def __repr__(self):
        return '<User %r>' % self.name


#Main Page
@app.route("/")
def index():
    return render_template('***')


#Map Page
@app.route("/map")
def map():
    return render_template('***')


#Search Page (For general sketch)
@app.route('/search/<name>')
def search(name):
    user = User.query.filter_by(name = name).first()
    return render_template('***', user = user)


# dynamic route: 
# 
# @app.route('/product/<int:product_id>')
# def product(product_id):
#    product = get_product_by_id(product_id)
#    return render_template('product.html', product=product)

# @app.route('/user/<string:username>')
# def user(username):
#     user = get_user_by_name(username)
#     return render_template('user.html', user=user)

# @app.route('/search/<search_query>')
# @app.route('/search/<search_query>/<int:page>')
# def search(search_query, page=1):
#     results = search_database(search_query, page)
#     return render_template('search.html', results=results)


#API Checking
valid_api_keys = {}
@app.route('/<api_key>/secure_route')
def secure_route(api_key):
    if api_key not in valid_api_keys:
        return jsonify(error = "Invalid API key"), 401
    return "This is a secure route"


#Bus Page
@app.route("/bus")
def bus():
    return render_template('***')


#Bus search
@app.route('/bus/<int:bus_id>')
def search_bus(bus_id):
    return f"This is the bus {bus_id}"
 #   return render_template('***')


  #  bus = search_database(search_query, page)
  #  return render_template('**HTML**', bus = bus)


#Stop Page
@app.route("/stop")
def stop():
    return render_template('***')


#Stop search
@app.route('/stop/<int:stop_id>')
def search_stop(stop_id):
    return f"This is the station {stop_id}"
#    return render_template('***')


#Route Page
@app.route("/route")
def route():
    return render_template('***')


#Route search
@app.route('/route/<int:sta_id>')
def search_route(sta_id):
    return f"This is the route {sta_id}"
#    return render_template('***')


#Q&A Page
@app.route("/qanda")
def qanda():
    return render_template('***')


#Contact Page
@app.route("/qanda/contact", methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
    return render_template('***')

if __name__ == "__main__":
    app.run(debug=True)