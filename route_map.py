import requests
import folium

start = input("Enter Start : ")
destination = input("Enter Destination : ")

response = requests.get(
    "http://127.0.0.1:8000/route",
    params={
        "start": start,
        "destination": destination
    }
)

data = response.json()

print("Response:", data)

if "geometry" not in data:
    print("No route geometry found!")
    exit()

geometry = data["geometry"]["coordinates"]

route_coords = [[lat, lon] for lon, lat in geometry]

m = folium.Map(location=route_coords[0], zoom_start=7)
folium.PolyLine(route_coords, weight=5).add_to(m)

m.save("route_map.html")
print("Map saved.")