import urllib.request
import json

f = urllib.request.urlopen("https://www.metaweather.com/api/location/44418")
print(f.status)
action = input("Dla jakiego miasta chcesz sprawdzić pogodę ? ")

data = (f.read())
data = json.loads(data)
print(data)
weather = (data[0]['consolidated_weather'])
for the_temp in weather:
    print(f"{temperatura['the_temp']}")

for air_pressure in weather:
    print(f"{cisnienie[air_pressure]}")

for humidity in weather:
    print(f"{wilgotnosc[humidity]}")

