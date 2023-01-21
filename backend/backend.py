from flask import Flask, render_template, request, jsonify
import functools


app = Flask(__name__)

@app.route("/")
def index():
    return 'MAIN PAGE'

@app.route("/map")
def map():
    return 'MAP PAGE'

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

valid_api_keys = {}
@app.route('/<api_key>/secure_route')
def secure_route(api_key):
    if api_key not in valid_api_keys:
        return jsonify(error = "Invalid API key"), 401
    return "This is a secure route"

@app.route("/bus")
def bus():
    return 'BUS PAGE'

@app.route('/bus/<int:bus_id>')
def bus_num(bus_id):
    return f"This is the bus {bus_id}"

  #  bus = search_database(search_query, page)
  #  return render_template('**HTML**', bus = bus)

@app.route("/stop")
def stop():
    return 'STOP PAGE'

@app.route('/stop/<int:stop_id>')
def stop_num(stop_id):
    return f"This is the station {stop_id}"

@app.route("/route")
def route():
    return 'ROUTE PAGE'

@app.route('/route/<int:sta_id>')
def route_num(sta_id):
    return f"This is the route {sta_id}"

@app.route("/qanda")
def qanda():
    return 'Q&A PAGE'

if __name__ == "__main__":
    app.run(debug=True)