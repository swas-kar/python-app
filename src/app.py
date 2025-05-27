from flask import Flask, jsonify
import datetime 
import socket

app = Flask(__name__)

@app.route('/api/v1/info')

def info():
    return jsonify({
        'time':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'hostname': socket.gethostname(),
        'message':'This is a cool app!',
        'deployed_on': 'Kubernetes'
    })

@app.route('/api/v1/healthz')

def healthz():
    return jsonify({
        'status': 'up'
    }),200

if __name__ == '__main__':

    app.run(host="0.0.0.0")

'/api/v1/info'
'/api/v1/healthz'