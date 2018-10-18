from airqo_device_monitor.external.thingspeak import (
    get_all_channel_ids,
    get_data_for_channel,
)
from airqo_device_monitor.data_entry import DataEntry


def get_and_format_data_for_channel(channel_id, start_time=None, end_time=None):
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
        entry_object.latitude = entry['field5']
        entry_object.longitute = entry['field6']
        entry_object.battery_voltage = entry['field7']

        entry_objects.append(entry_object)
    return entry_objects


def get_and_format_data_for_all_channels(start_time=None, end_time=None):
    channel_ids = get_all_channel_ids()

    all_channels_dict = dict()
    for channel_id in channel_ids:
        data = get_and_format_data_for_channel(channel_id, start_time=start_time, end_time=end_time)
        all_channels_dict[channel_id] = data

    return all_channels_dict
