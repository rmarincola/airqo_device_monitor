class DataEntry(object):

    def __init__(self, channel_id, entry_id):
        self.channel_id = channel_id
        self.entry_id = entry_id

    created_at = None
    channel_id = None
    entry_id = None
    pm_1 = None
    pm_2_5 = None
    pm_10 = None
    sample_period = None
    latitude = None
    longitute = None
    battery_voltage = None
    elevation = None
