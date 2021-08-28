import requests
import json
def string(s):
    data={"address":s,"key":"AIzaSyDTgcZY0M3Ma7O49qFmhq4d-4mGpv3WBU4"}
    response=requests.get("https://maps.googleapis.com/maps/api/geocode/json",params=data)
    localjson=json.loads(response.text)
    r=localjson["results"][0]["geometry"]["location"]
    #print("Coordinates of", s,":",r)
    return str(r["lat"])+","+str(r["lng"])