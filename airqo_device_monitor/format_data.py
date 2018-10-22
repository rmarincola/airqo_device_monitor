from airqo_device_monitor.external.thingspeak import (
    get_all_channel_ids,
    get_data_for_channel,
)
from airqo_device_monitor.models.data_entry import DataEntry


def parse_lat_lng_elevation(lat_lng_elevation_str):
    """
    Parse string formatted lat,lng,elevation into three variables
    """
    return lat_lng_elevation_str.split(',')


def get_and_format_data_for_channel(channel_id, start_time=None, end_time=None):
    """
    Parses thingspeak json response.
    Field mapping:
    field1: pm1
    field2: pm2.5
    field3: pm10
    field4: sample period
    field5: latitude
    field6: longtitude
    field7: battery voltage
    field8 (optional): lat,lng,elevation
    """
    data = get_data_for_channel(channel_id, start_time=start_time, end_time=end_time)
    entry_objects = []
    for entry in data:
        entry_object = DataEntry(
            channel_id=channel_id,
            entry_id=entry['entry_id'],
        )
        entry_object.created_at = entry['created_at']
        entry_object.pm_1 = entry['field1']
        entry_object.pm_2_5 = entry['field2']
        entry_object.pm_10 = entry['field3']
        entry_object.sample_period = entry['field4']
        entry_object.battery_voltage = entry['field7']

        lat_lng_elevation = entry.get('field8', None)
        if lat_lng_elevation:
            lat, lng, elevation = parse_lat_lng_elevation(lat_lng_elevation)
            entry_object.latitude = lat
            entry_object.longitude = lng
            entry_object.elevation = elevation
        else:
            entry_object.latitude = entry['field5']
            entry_object.longitude = entry['field6']

        entry_objects.append(entry_object)
    return entry_objects


def get_and_format_data_for_all_channels(start_time=None, end_time=None):
    channel_ids = get_all_channel_ids()

    all_channels_dict = dict()
    for channel_id in channel_ids:
        data = get_and_format_data_for_channel(channel_id, start_time=start_time, end_time=end_time)
        all_channels_dict[channel_id] = data

    return all_channels_dict
