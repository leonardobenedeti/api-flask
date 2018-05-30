from flask import Flask, jsonify

app = Flask(__name__)

class Cards:
	def __init__(self, title, desc )
		self.title = title
		self.desc = desc

listCards = { Cards('Amazing Card #1', 'Card to show how works jsonifi by flask #1'), Cards('Amazing Card #2', 'Card to show how works jsonifi by flask #2')} 

@app.route('/')
def index():
	return jsonify(listCards)

if __name__ == "__main__":
	app.run()