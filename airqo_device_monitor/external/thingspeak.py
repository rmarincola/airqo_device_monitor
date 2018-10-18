import json, requests
from datetime import datetime, timedelta

from airqo_device_monitor.constants import (
    DEFAULT_THINGSPEAK_DATA_INTERVAL_DAYS,
    THINGSPEAK_API_MAX_NUM_RESULTS,
    THINGSPEAK_CHANNELS_LIST_URL,
    THINGSPEAK_FEEDS_LIST_URL,
    MATHWORKS_USER_ID,
)


def get_data_for_channel(channel, start_time=None, end_time=None):
    if not start_time:
        start_time = datetime.now() - timedelta(days=DEFAULT_THINGSPEAK_DATA_INTERVAL_DAYS)
    if not end_time:
        end_time = datetime.now()

    # convert to string before the loop because this never changes
    start_time_string = datetime.strftime(start_time,'%Y-%m-%dT%H:%M:%SZ')

    api_url = THINGSPEAK_FEEDS_LIST_URL.format(channel)
    all_data = []

    while start_time <= end_time:
        full_url = '{}/feeds/?start={}&end={}'.format(
            api_url,
            start_time_string,
            datetime.strftime(end_time,'%Y-%m-%dT%H:%M:%SZ'),
        )
        result = make_post_call(full_url)

        feeds = result['feeds']
        all_data.extend(feeds)

        # If we aren't hitting the max number of results then we
        # have all of them for the time range and can stop iterating
        if len(feeds) < THINGSPEAK_API_MAX_NUM_RESULTS:
            break

        first_result = feeds[0]
        end_time = datetime.strptime(first_result['created_at'],'%Y-%m-%dT%H:%M:%SZ') - timedelta(seconds=1)

    return all_data


def get_all_channel_ids():
    url = THINGSPEAK_CHANNELS_LIST_URL.format(MATHWORKS_USER_ID)
    response = make_get_call(url)

    channels = response['channels']
    channel_ids = [channel['id'] for channel in channels]

    return channel_ids


def make_post_call(url):
    return json.loads(requests.post(url).content)


def make_get_call(url):
    return json.loads(requests.get(url).content)
