# OSM-Route-Nav

A simple **FastAPI project** that converts place names into coordinates and finds the **driving route** between two locations using:

* **Nominatim (OpenStreetMap)** → for geocoding
* **OSRM (Open Source Routing Machine)** → for route calculation

This project is useful for learning:

* APIs
* Geolocation services
* Route calculation
* FastAPI backend development

---

## 🚀 Features

* Convert a location name into **latitude and longitude**
* Get the **driving route** between two places
* Return:

  * Start location
  * Destination
  * Distance in km
  * Duration in minutes
  * Route geometry in GeoJSON format

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Nominatim API**
* **OSRM API**

---

## 📂 Project Structure

```bash
project/
│── main.py
│── requirements.txt
│── README.md
```

---

## ▶️ Run the Project

Start the FastAPI server using:

```bash
uvicorn main:app --reload
```

Server will run at:

```bash
http://127.0.0.1:8000
```

---

## 📌 API Endpoints

## 1. `/geocode`

Convert a location name into coordinates.

### **Endpoint**

```http
GET /geocode?location=Paris
```

### **Example Request**

```bash
http://127.0.0.1:8000/geocode?location=Pune
```

### **Example Response**

```json
{
  "latitude": 18.5214,
  "longitude": 73.8545,
  "display_name": "Pune, Maharashtra, India"
}
```

---

## 2. `/route`

Get the driving route between two places.

### **Endpoint**

```http
GET /route?start=Pune&destination=Mumbai
```

### **Example Request**

```bash
http://127.0.0.1:8000/route?start=Pune&destination=Mumbai
```

### **Example Response**

```json
{
  "from": "Pune, Maharashtra, India",
  "to": "Mumbai, Maharashtra, India",
  "distance_km": 149.27,
  "duration_minutes": 181.45,
  "geometry": {
    "coordinates": [
      [73.8567, 18.5204],
      [73.9000, 18.6000]
    ],
    "type": "LineString"
  }
}
```

---

## 🧪 API Docs

After running the app, open:

### Swagger UI

```bash
http://127.0.0.1:8000/docs
```


## 💡 Example Use Cases

* Location search apps
* Navigation systems
* Map-based backend projects

---

## ⚠️ Notes

* This project uses **free public APIs**, so response speed and availability may vary.

---

Made with FastAPI for learning geolocation and routing APIs.
