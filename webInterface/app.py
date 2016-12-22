from flask import Flask
from flask.ext.bower import Bower
app = Flask(__name__)
@app.route("/")
def main():
	return "wrong thing"

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     WSGIServer(('0.0.0.0', int(os.environ.get("PORT", 5000))), app).serve_forever()


if __name__ == "__main__":
	port = int(os.environ.get("PORT"),5000)
	app.run('0.0.0.0',port=port,debug=True)
Bower(app)
