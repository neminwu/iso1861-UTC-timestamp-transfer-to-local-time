import json

# Using Bing Maps API
BING_MAPS_KEY ="Paste your own key here"


def get_local_time(lon,lat,isotime_utc):
    try: 
        r = requests.get(
        f"https://dev.virtualearth.net/REST/v1/TimeZone/{lat},{lon}?datetime={isotime_utc}&key={BING_MAPS_KEY}")
    
        return r.json()['resourceSets'][0]['resources'][0]['timeZone']['convertedTime']['localTime']
    except:
        return "NA"
        

def get_time_zone(lon,lat,isotime_utc):
    try: 
        r = requests.get(
        f"https://dev.virtualearth.net/REST/v1/TimeZone/{lat},{lon}?datetime={isotime_utc}&key={BING_MAPS_KEY}")
    
        return r.json()['resourceSets'][0]['resources'][0]['timeZone']
    except:
        return "NA"
        
 #test
 print(get_local_time(-78.853563,42.8962295,"2019-03-31T23:57:12.000Z"))
 print(get_time_zone(-78.853563,42.8962295,"2019-03-31T23:57:12.000Z"))