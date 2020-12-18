from flask import Flask, jsonify

app = Flask(__name__)


def build_message(parent, data, field=''):
	return_value = []
	for d in data:
		to_append = (d + ": " + str(data[d])) if (field == '') else (d[field])
		return_value.append(to_append)
	return jsonify({parent: return_value})


def initialize():
	app.run(debug=True)
