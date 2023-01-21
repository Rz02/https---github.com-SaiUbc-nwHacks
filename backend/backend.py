from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'MAIN PAGE'

@app.route("/map")
def map():
    return 'MAP PAGE'

@app.route("/bus")
def bus():
    return 'BUS PAGE'

@app.route('/bus/<int:id>')
def bus_num(id):
    return f"This is the bus {id}"

@app.route("/station")
def station():
    return 'STATION PAGE'

@app.route('/station/<int:id>')
def station_num(id):
    return f"This is the station {id}"

@app.route("/qanda")
def qanda():
    return 'Q&A PAGE'

if __name__ == "__main__":
    app.run(debug=True)