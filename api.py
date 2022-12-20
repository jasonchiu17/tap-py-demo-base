from flask import Blueprint, jsonify

app2 = Blueprint('app2', __name__)

@app2.route('/api')
def api():
    resp = { 
    'data' : { 
        'd1': 'hello world',
        'd2': 'test'
    } ,
    'info' : { 
        'app_name' : 'TAP python demo',
        'data_from' : 'ZERONE'
        }
    }
    return jsonify(resp)

@app2.route('/ping')
def ping():
    return jsonify(ping='pong')
