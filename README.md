# Transfer iso1861/UTC/timestamp to local time
transfer iso1861/UTC/timestamp to local time, based on coordinate(longtitude&amp;latitude)/time zone. The two methods bring out the same results, while the Method 1 works faster.
## Method 1. Based on Bing Map API
This method is based on bing map API https://docs.microsoft.com/en-us/bingmaps/rest-services/timezone/convert-local-time-zone  
You need to apply for a Bing Map API Key here: https://www.microsoft.com/en-us/maps/create-a-bing-maps-key  
  
    
## Method 2. Use datetime and pytz library
To use this mehtod you need to pip install the libraries listed in the requirements.txt


