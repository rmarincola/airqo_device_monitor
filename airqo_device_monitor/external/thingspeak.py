import json, requests
from datetime import datetime, timedelta

from airqo_device_monitor.constants import (
    DEFAULT_THINGSPEAK_DATA_INTERVAL_DAYS,
    THINGSPEAK_API_URL,
)


def get_data_for_channel(channel, start_time=None, end_time=None):
    if not start_time:
        start_time = datetime.now() - timedelta(days=DEFAULT_THINGSPEAK_DATA_INTERVAL_DAYS)
    if not end_time:
        end_time = datetime.now()

    api_url = THINGSPEAK_API_URL.format(channel)
    all_data = []

    while start_time < end_time:
        full_url = '{}/feeds/?start={}&end={}'.format(api_url, start_time, end_time)
        result = json.loads(requests.post(full_url).content)

        alldata.extend(data['feeds'])

        if len(result) < 8000:
            break

        last_result = result[len(result)-1]
        start_time = datetime.strptime(last_result['created_at'],'%Y-%m-%dT%H:%M:%SZ')

    return all_data


# import pdb; pdb.set_trace()
print "running..."
print get_data_for_channel(295702)

# nextid = 1
# result = None
# alldata = []
# endtime = None

# while result != '-1' and result != -1:
#     print nextid
#     result = json.loads(requests.post(apiurl+'/feeds/entry/%d.json' % nextid).content)

#     starttime = endtime
#     if result == '-1' or result == -1:
#         endtime = datetime.now()
#     else:
#         endtime = datetime.strptime(result['created_at'],'%Y-%m-%dT%H:%M:%SZ')
#     if (nextid==1):
#         starttime = endtime
#     else:
#         start = datetime.strftime(starttime,'%Y-%m-%dT%H:%M:%SZ')
#         end = datetime.strftime(endtime-timedelta(seconds=1),'%Y-%m-%dT%H:%M:%SZ')
#         data = json.loads(requests.post(apiurl+'/feeds.json?start=%s&end=%s' % (start,end)).content)
#         print nextid, len(data['feeds'])
#         alldata.extend(data['feeds'])
#     nextid += 7999 #thought download was 8000 fields, but it's 8000 records. 8000/len(result)
