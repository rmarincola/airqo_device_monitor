import json, requests
from datetime import datetime, timedelta

from airqo_device_monitor.constants import THINGSPEAK_API_URL


def get_data_for_channel(channel, start_time=None, end_time=None):
	pass


# nextid = 1
# result = None
# alldata = []
# endtime = None

# while result != '-1' and result != -1:
#     print nextid
#     result = json.loads(requests.post(THINGSPEAK_API_URL+'/feeds/entry/%d.json' % nextid).content)

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
#         data = json.loads(requests.post(THINGSPEAK_API_URL+'/feeds.json?start=%s&end=%s' % (start,end)).content)
#         print nextid, len(data['feeds'])
#         alldata.extend(data['feeds'])
#     nextid += 7999 #thought download was 8000 fields, but it's 8000 records. 8000/len(result)
