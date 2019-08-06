from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone

inputformat="%Y-%m-%d %H:%M:%S.%f%z"
outputformat="%Y%m%d_%H%M"

sampled="2019-08-05 08:52:49.193254+03:00"

def converttolocalzone(inputtimestamp=None):
    inputtimestamp=inputtimestamp.replace("T"," ")
    d=inputtimestamp
    if ":" == d[-3:-2]:
        d = d[:-3]+d[-2:]
    datetime_object = datetime.strptime(d, inputformat)
    print(datetime_object)
    print(get_localzone())
    now_local = datetime_object.astimezone(get_localzone())
    return (now_local.strftime(outputformat))

print(converttolocalzone(sampled))
