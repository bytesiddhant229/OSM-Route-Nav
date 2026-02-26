from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
OSRM_BASE_URL = "https://router.project-osrm.org/route/v1/driving"

async def geocode(location: str):
    params = {
        "q": location,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "OSMrn"
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            NOMINATIM_URL,
            params=params,
            headers=headers
        )

    data = response.json()

    if not data:
        raise HTTPException(status_code=404, detail=f"{location} not found")

    return {
        "latitude": float(data[0]["lat"]),
        "longitude": float(data[0]["lon"]),
        "display_name": data[0]["display_name"]
    }

@app.get("/geocode")
async def get_geocode(location: str):
    result = await geocode(location)
    return result



@app.get("/route")
async def get_route(start : str, destination: str):

    start = await geocode(start)
    end = await geocode(destination)

    route_url = (
        f"{OSRM_BASE_URL}/"
        f"{start['longitude']},{start['latitude']};"
        f"{end['longitude']},{end['latitude']}"
    )

    params = {
        "overview": "full",
        "geometries": "geojson"
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(route_url, params=params)

    route_data = response.json()

    if route_data.get("code") != "Ok":
        raise HTTPException(status_code=400, detail="Route not found")

    route = route_data["routes"][0]

    return {
        "from": start["display_name"],
        "to": end["display_name"],
        "distance_km": round(route["distance"] / 1000, 2),
        "duration_minutes": round(route["duration"] / 60, 2),
        "geometry": route["geometry"]
    }