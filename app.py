from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():  # put application's code here
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)