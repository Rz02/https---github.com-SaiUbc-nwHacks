#this file is for the google maps platform integration 
from flask import Flask, render_template
from tilapya import *
api = RTTI('Ik7TSY2bkJRQzeQeH5LT')

app = Flask("mapAPI")

@app.route('/stop_name/<float:lat>/<float:lng>')
def stopCoords(stop_num):
    stop = api.stop(stop_num)
    return render_template('./frontend/map.html', stop.Latitude, stop.Longitude)

if __name__ == 'mapAPI':
    app.run()