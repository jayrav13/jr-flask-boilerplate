# Flask Boilerplate
# By Jay Ravaliya

from flask import Flask, make_response, jsonify, request, abort, render_template
from flask.ext.assets import Environment, Bundle
import requests

app = Flask(__name__)

assets = Environment(app)
css = Bundle('css/styles.css', output='get/packed.css')
assets.register('css_all', css)

@app.route("/", methods=['GET','POST'])
def home():
	return make_response(jsonify({"Success" : "Hello, world!"}), 200)

@app.route("/template", methods=['GET'])
def template():
	return render_template('index.html')

@app.route("/jr-flask-boilerplate", methods=['GET'])
def about_boilerplate():
	return make_response(jsonify({"By" : "Jay Ravaliya"}), 200)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
