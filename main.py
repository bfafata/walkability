import coords
import findnearby
import travel
import score
print("Walkability score")
homeaddress=input("Enter your address:")
homecoords=coords.string(homeaddress)

#Types of establishments and weightings
types={
    "grocery":2.5,
    "coffee":1,
    "park":1.5,
    "food":1,
    "school" :1.25
}


timelist=[]
for item in list(types.keys()):
    print(f"Closest {item}:")
    res=findnearby.find(homecoords,item)

    if res["status"]=="ZERO_RESULTS":
        print("None found within 2000 meters")

    else:
        address=res["candidates"][0]["formatted_address"]
        name=res["candidates"][0]["name"]

        print(f"{name} at {address}")

        time=travel.time(homeaddress,address)
        formattedtime="{:.2f}".format(time/60)
        print(f"{formattedtime} minutes away")
        timelist.append(time/60)

walkabilityscore="{:.2f}".format(score.timescore(timelist,list(types.values())))
print(f"Walkability score:{walkabilityscore}/100")
