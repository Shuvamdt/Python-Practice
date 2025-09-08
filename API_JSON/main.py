import requests as req
import datetime as dt

MY_LAT = 22.568080
MY_LNG = 88.510160

# res = req.get(url="http://api.open-notify.org/iss-now.json")
# res.raise_for_status()
#
# data = res.json()["iss_position"]
# lat = data["latitude"]
# lon = data["longitude"]
#
# iss = (lat, lon)
#
# print(iss)

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted" : 0
}

res = req.get(url="https://api.sunrise-sunset.org/json", params=params)
res.raise_for_status()
data = res.json()["results"]
sunrise = data["sunrise"]
sunset = data["sunset"]
print(sunrise," ", sunset)
print(dt.datetime.now().hour)