from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


@app.route("/video")
def video():
    return "Getting Video Sync Status!"

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port='8080'
    )

