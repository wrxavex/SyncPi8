from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"
    cpu_temp_raw_data = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
    get_cpu_temp = cpu_temp_raw_data.strip()
    return get_cpu_temp


@app.route("/video")
def video():
    return "Getting Video Sync Status!"

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port='8080'
    )

