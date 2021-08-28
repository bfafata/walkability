import requests
import json
tc="40.44528145234949,-79.94876966741371"
tc2="40.49782465431407,-79.97850043899813"
tc3="40.4657338139507,-79.942742874511"

#
def find(coordsoforigin,inp):
    data={"input":inp,"inputtype":"textquery", "locationbias":f"point:{coordsoforigin}","fields":"name,formatted_address,type","key":"AIzaSyDTgcZY0M3Ma7O49qFmhq4d-4mGpv3WBU4"}
    testresponse=requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json",params=data)
    testjson=json.loads(testresponse.text)
    #print(json.dumps(testjson,indent=4))

    return testjson
