import requests
from typing import Tuple, Dict, Any
from google.adk.agents import Agent

# --- constants & session ---
BASE_GEO_URL     = "https://geocoding-api.open-meteo.com/v1/search"
BASE_FORECAST_URL= "https://api.open-meteo.com/v1/forecast"
BASE_TZ_URL      = "https://api.open-meteo.com/v1/timezone"
TIME_API_URL     = "https://timeapi.io/api/time/current/zone"

TIMEOUT          = 5
_session         = requests.Session()

# --- helper ---
def _geocode_city(city: str) -> Tuple[float, float]:
    resp = _session.get(BASE_GEO_URL, params={"name": city, "count": 1}, timeout=TIMEOUT)
    resp.raise_for_status()
    results = resp.json().get("results")
    if not results:
        raise ValueError(f"City '{city}' not found.")
    loc = results[0]
    return loc["latitude"], loc["longitude"], loc["timezone"]

# --- tools ---
def get_weather(city: str) -> Dict[str, Any]:
    try:
        lat, lon, _ = _geocode_city(city)
        resp = _session.get(
            BASE_FORECAST_URL,
            params={"latitude": lat, "longitude": lon, "current_weather": True},
            timeout=TIMEOUT
        )
        resp.raise_for_status()
        cw = resp.json().get("current_weather", {})
        report = (
            f"The weather in {city} is {cw.get('temperature')}°C, "
            f"wind speed {cw.get('windspeed')} m/s, code {cw.get('weathercode')}."
        )
        return {"status": "success", "report": report, "data": cw}
    except (requests.RequestException, ValueError) as e:
        return {"status": "error", "error_message": str(e)}

def get_current_time(city: str) -> Dict[str, Any]:
    try:
        _, _, tz = _geocode_city(city)
        resp = _session.get(TIME_API_URL, params={"timeZone": tz}, timeout=TIMEOUT)
        resp.raise_for_status()
        time_data = resp.json()
        # Format the report
        report = f"The current time in {city} is {time_data.get('time')} ({time_data.get('timeZone')})."
        
        return {
            "status": "success", 
            "report": report, 
            "data": {
                "current_time": time_data.get('time'),
                "timezone": time_data.get('timeZone'),
                "date": time_data.get('date'),
                "day_of_week": time_data.get('dayOfWeek')
            }
        }
    except (requests.RequestException, ValueError) as e:
        return {"status": "error", "error_message": str(e)}


AUDIO_MODEL = "gemini-2.0-flash-audio-001"
CONTENT_MODEL = "gemini-2.0-flash"
# --- agent setup  ---
root_agent = Agent(
    name="weather_time_agent",
    model=CONTENT_MODEL,
    description="Agent to answer questions about the time and weather in a city.",
    instruction="""
You are a specialized weather and time assistant that provides accurate information for cities worldwide.

YOUR CAPABILITIES:
- Retrieve current weather conditions including temperature, wind speed, and weather code
- Find the current local time for any city around the globe

RESPONSE GUIDELINES:
- Always respond in a friendly, conversational tone
- Provide complete information in your answers
- If user asks about weather, include temperature, wind conditions, and what the weather code means
- If user asks about time, include the local time and timezone
- If a city cannot be found or another error occurs, politely explain the issue

EXAMPLES:
User: "What's the weather like in Tokyo?"
Assistant: "The current weather in Tokyo is 23°C with wind speeds of 4.2 m/s. The weather code 0 means clear sky."

User: "What time is it in London?"
Assistant: "The current time in London is 14:35 (GMT)."

User: "Tell me about the weather and time in Paris"
Assistant: "In Paris, it's currently 18°C with wind speeds of 3.7 m/s (light breeze). The local time is 15:35 (CET)."
""",
    tools=[get_weather, get_current_time],
)

# for voice testing, dont forget to export SSL_CERT_FILE=$(python -m certifi)