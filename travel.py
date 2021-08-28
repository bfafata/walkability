import requests
import json
def time(org,des):
    if des==0:
        return 0
    data={"origin":org,"destination":des,"mode":"walking","key":"AIzaSyDTgcZY0M3Ma7O49qFmhq4d-4mGpv3WBU4"}
    testresponse=requests.get("https://maps.googleapis.com/maps/api/directions/json",params=data)
    testjson=json.loads(testresponse.text)
    #return {"dist": testjson["routes"][0]["legs"][0]["distance"]["value"],"time":testjson["routes"][0]["legs"][0]["duration"]["value"]}
    return testjson["routes"][0]["legs"][0]["duration"]["value"]