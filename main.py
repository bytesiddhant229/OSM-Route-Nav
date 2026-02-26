from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

@app.get("/geodata")
async def get_geodata(location: str):
    
    params = {
        "q": location,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "OSMrn"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(NOMINATIM_URL, params=params, headers=headers)

    data = response.json()

    if not data:
        raise HTTPException(status_code=404, detail="Location not found")

    return {
        "location": location,
        "latitude": data[0]["lat"],
        "longitude": data[0]["lon"],
        "display_name": data[0]["display_name"]
    }
