from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(title="Svetlana's Learning Backend")

# Настройка CORS (уже знакомо)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# 1. Health Check
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Server is running"}


# 2. User Info (симуляция базы данных)
@app.get("/user")
def get_user():
    return {
        "name": "Svetlana Pulucciu",
        "email": "svetlana.pulucciu250693@gmail.com",
        "role": "Project Manager",
        "city": "Chisinau"
    }


# 3. Weather API (внешний вызов)
@app.get("/weather")
def get_weather(city: str = "Chisinau"):
    # Сначала ищем координаты города
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_resp = requests.get(geo_url).json()

    if not geo_resp.get("results"):
        raise HTTPException(status_code=404, detail="City not found")

    lat = geo_resp["results"][0]["latitude"]
    lon = geo_resp["results"][0]["longitude"]

    # Теперь получаем погоду по координатам
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_resp = requests.get(weather_url).json()

    return {
        "city": city,
        "temperature": weather_resp["current_weather"]["temperature"],
        "unit": "°C"
    }


# 4. Pokemons API (внешний вызов)
@app.get("/pokemons")
def get_pokemons(count: int = 5):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={count}"
    resp = requests.get(url).json()
    names = [p["name"] for p in resp["results"]]
    return {"count": count, "pokemons": names}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)