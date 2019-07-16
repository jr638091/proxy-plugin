from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app)

@app.route('/account/info', methods= ['POST'])
@cross_origin()
def get_info():
	if not request.json or not 'username' in request.json or not 'password' in request.json or not 'type' in request.json:
		abort(404)
	else:
		username = request.json['username']
		password = request.json['password']
		tipo = request.json['type']

		# buscar estado de la cuenta

		basico = 100
		extra = 100
		consumido = 150

		return jsonify({'basico': basico, 'extra': extra, 'consumido': consumido})

if __name__ == '__main__':
    app.run(host='192.168.1.106', port='5000', debug=True, ssl_context=('certs', 'ca.key'))