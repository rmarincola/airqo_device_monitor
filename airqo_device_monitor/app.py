from flask import (
    Flask,
    jsonify,
    render_template,
)

from airqo_device_monitor.external.thingspeak import get_all_channel_ids

app = Flask(__name__)

@app.route('/')
def get_malfunctioning_channels():
    malfunctioning_channels = get_all_channel_malfunctions()
    return render_template(
        "index.html",
        malfunctioning_channels=malfunctioning_channels,
    )


if __name__ == "__main__":
    app.run(debug=True)
