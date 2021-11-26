import datetime
import os
import requests
from tzwhere import tzwhere
from pytz import timezone
import datetime
import pytz
import time
from dateutil import parser


#iso to timestamp
import datetime,pytz

#transfer ISO8601 to timestamp
def iso2timestamp(datestring, format='%Y-%m-%dT%H:%M:%S.%fZ',timespec='seconds'):
   
    tz = pytz.timezone('Asia/Shanghai')
    utc_time = datetime.datetime.strptime(datestring, format)  # 将字符串读取为 时间 class datetime.datetime

    time = utc_time.replace(tzinfo=pytz.utc).astimezone(tz)

    times = {
        'seconds': int(time.timestamp()),
        'milliseconds': round(time.timestamp() * 1000),
        'microseconds': round(time.timestamp() * 1000 * 1000),
    }
    return times[timespec]
    
 def get_local_time(lon,lat,isotime_utc):
    
    try: 
        #iso to timestamp
        timestamp = iso2timestamp(isotime_utc)
    
        #timestamp, lat, lon to local_time
        tz = tzwhere.tzwhere(forceTZ=True)
        time_zone = tz.tzNameAt(lat,lon, forceTZ=True)  #纬度，经度。 得到对应的时区
    
        local_time = datetime.datetime.fromtimestamp(timestamp,pytz.timezone(time_zone)).strftime('%Y-%m-%d %H:%M:%S')
    
        return local_time
    
    except:
        return "N/A"  
    
def get_time_zone(lon,lat,isotime_utc):
    
    try: 
        #iso to timestamp
        timestamp = iso2timestamp(isotime_utc)
    
        #timestamp, lat, lon to local_time
        tz = tzwhere.tzwhere(forceTZ=True)
        time_zone = tz.tzNameAt(lat,lon, forceTZ=True)  #纬度，经度。 得到对应的时区
    
        #local_time = datetime.datetime.fromtimestamp(timestamp,pytz.timezone(time_zone)).strftime('%Y-%m-%d %H:%M:%S')
    
        return time_zone
    
    except:
        return "N/A"  
        
 #test
 print(get_local_time(-78.853563,42.8962295,"2019-03-31T23:57:12.000Z"))
 print(get_time_zone(-78.853563,42.8962295,"2019-03-31T23:57:12.000Z"))