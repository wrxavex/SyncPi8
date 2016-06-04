from flask import Flask
from flask import render_template
import os
import time
import subprocess
import NoButtonVideoSync as VideoSync

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def home(name=None, cputemp=None, result=None, videoinLocalSize=None, videoinUsbSize=None, sync_status=None):
    cpu_temp_raw_data = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
    sync_status_result = subprocess.check_output(["ps", "ax", "|", "grep", "-v", "grep", "|", "grep", "omxplayer-sync"])
    get_cpu_temp = cpu_temp_raw_data.strip()
    videostatus = VideoSync.main(VideoSync.usb_video_file)
    result = VideoSync.result
    videoinLocalSize = VideoSync.videoinLocalSize
    videoinUsbSize = VideoSync.videoinUsbSize
    return render_template('home.html',name=name, cputemp=get_cpu_temp, result=result, videoinLocalSize=videoinLocalSize, videoinUsbSize=videoinUsbSize, sync_status=sync_status_result)


@app.route("/video")
def video():
    return "Getting Video Sync Status!"

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port='8080'
    )

