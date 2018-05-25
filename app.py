from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "API básica em Flask deploiada no heroku!"

if __name__ == "__main__":
	app.run()