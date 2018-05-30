from flask import Flask, jsonify
import json

app = Flask(__name__)

card1 = {'title':'Amazing Card #1', 'desc':'Card to show how works jsonifi by flask #1'}
card2 = {'title':'Amazing Card #2', 'desc':'Card to show how works jsonifi by flask #2'}
listCards = {'cards':[card1, card2]}

@app.route('/', methods=["GET",])
def index():
	return jsonify(listCards)

if __name__ == "__main__":
	app.run(debug=True)