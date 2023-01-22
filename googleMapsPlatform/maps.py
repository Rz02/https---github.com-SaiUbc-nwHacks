#this file is for the google maps platform integration 
from flask import Flask, render_template

app = Flask("mapAPI")

@app.route('/bus_location/<float:lat>/<float:lng>')
def update_bus_location(lat, lng):
    return render_template('./frontend/map.html', lat=lat, lng=lng)

if __name__ == 'mapAPI':
    app.run()