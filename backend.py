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

@app.route("/station")
def station():
    return 'STATION PAGE'

@app.route("/Q&A")
def qanda():
    return 'Q&A PAGE'

if __name__ == "__main__":
    app.run(debug=True)