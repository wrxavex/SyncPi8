from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/video")
def hello():
    return "Getting Video Sync Status!"

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port='6666'
    )

