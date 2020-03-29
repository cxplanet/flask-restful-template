from api import app
from flask import jsonify

@app.route("/")
def status():
    return jsonify({'status':{'code': 200, 'message':"Everything's shiny captain, not to fret"}, 'data':{'version': '1.0'}})
