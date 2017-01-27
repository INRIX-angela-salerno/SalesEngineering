           #urlDataLoop = "http://odotloc.dot.state.oh.us/?lat=" + str(latitude) + "&lon=" + str(longitude)
import urllib3
import json

latitude = "39.348034"
longitude = "-82.95947899"

urlDataLoop = "http://odotloc.dot.state.oh.us/?lat=" + latitude + "&lon=" + longitude
#print(urlDataLoop)
http = urllib3.PoolManager()
    
rLoop = http.request('GET', urlDataLoop)
#print(rLoop.data)

theJSONLoop = json.loads(rLoop.data.decode('utf-8'))

if "LogpointStateNbr":
    print("Latitude: " + str(theJSONLoop["ComputedLatitude"]))
    print("Longitude: " + str(theJSONLoop["ComputedLongitude"]))
    print("MileMarker: " + str(theJSONLoop["LogpointStateNbr"]))
