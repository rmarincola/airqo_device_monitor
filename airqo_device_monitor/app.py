from flask import (
    Flask,
    jsonify,
    render_template,
)

from airqo_device_monitor.external.thingspeak import get_all_channel_ids

app = Flask(__name__)

@app.route('/')
def get_malfunctioning_channels():
    mock_response = {99649: ['no_data'], 183070: ['no_data'], 223586: ['no_data'], 241694: [], 265435: [], 268271: ['no_data'], 284171: ['no_data'], 295702: ['low_reporting_frequency'], 309890: ['low_battery_voltage', 'low_reporting_frequency'], 312183: ['no_data'], 318099: ['low_reporting_frequency'], 324682: ['low_reporting_frequency'], 327840: ['low_battery_voltage', 'low_reporting_frequency'], 403696: ['no_data']}

    # import pdb; pdb.set_trace()
    # return render_template("index.html", malfunctions=jsonify(mock_response).data)
    return render_template("index.html", malfunctions=mock_response)


if __name__ == "__main__":
    app.run(debug=True)