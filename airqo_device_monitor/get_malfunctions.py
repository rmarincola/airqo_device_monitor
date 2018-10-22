from airqo_device_monitor.format_data import get_and_format_data_for_all_channels
from datetime import datetime, timedelta


def _get_channel_malfunctions(channel_data):
    """Use channel_data to get a list of malfunctions that may be occuring with a channel."""
    malfunction_list = []
    if _has_low_battery(channel_data):
        malfunction_list.append("low_battery_voltage")
    if _has_low_reporting_frequency(channel_data):
        malfunction_list.append("low_reporting_frequency")
    if _sensor_is_reporting_outliers(channel_data):
        malfunction_list.append("reporting_outliers")
    return malfunction_list


def _has_low_battery(channel_data):
    """Determine whether the channel has low battery."""
    last_voltage = float(channel_data[-1].battery_voltage)
    return last_voltage < LOW_BATTERY_CUTOFF


def _has_low_reporting_frequency(channel_data):
    """Determine whether the channel is reporting data at a lower frequency than expected."""
    index_to_verify = min(len(channel_data), NUM_REPORTS_TO_VERIFY_MALFUNCTION)
    report_to_verify = channel_data[-1 * index_to_verify]
    time_to_submit_reports = datetime.strptime(report_to_verify.created_at, '%Y-%m-%dT%H:%M:%SZ')
    cutoff_time = datetime.utcnow() - timedelta(MAXIMUM_MINUTES_PER_REPORT * index_to_verify)
    return time_to_submit_reports < cutoff_time


def _sensor_is_reporting_outliers(channel_data):
    """Determine whether the sensor is reporting points outside the reasonable range.

    Presence of outlier points may indicated an obstructed sensor.
    """
    num_points = min(NUM_REPORTS_TO_VERIFY_SENSOR_MALFUNCTION, len(channel_data))
    is_outlier = lambda pm_2_5: pm_2_5 < SENSOR_PM_2_5_MIN_CUTOFF or pm_2_5 > SENSOR_PM_2_5_MAX_CUTOFF
    extreme_reads = [entry for entry in channel_data[-1 * num_points:] if is_outlier(float(entry.pm_2_5))]
    for point in extreme_reads:
        print point.pm_2_5
    return len(extreme_reads) > num_points * ALLOWABLE_OUTLIER_SENSOR_RATIO

def get_all_channel_malfunctions():
    """Generate a list of malfunctions for all channels.

    Returns: A dict keyed by the channel id. The value is a list of potential concerns about a sensor.
    """
    malfunctions = {}
    start_time = datetime.utcnow() - timedelta(days=1)
    all_data = get_and_format_data_for_all_channels(start_time=start_time)
    empty_channels = [key for key in data.keys() if len(data[key]) == 0]
    for channel_id in empty_channels:
        malfunctions[channel_id] = ["no_data"]

    usable_data = {key: val for key, val in data.items() if len(val) > 0}
    for channel_id, channel_data in public_data.items():
        malfunctions[channel_id] = _get_channel_malfunctions(channel_data)

    return malfunctions