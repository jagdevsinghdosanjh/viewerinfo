import requests
import streamlit as st

def get_geo():
    try:
        # Get IP from Streamlit headers
        ip = st.context.headers.get("X-Forwarded-For", "").split(",")[0].strip()

        if not ip:
            return {"error": "No IP detected"}

        # Use a free geolocation API
        url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return {"error": "Geo API failed"}

        data = response.json()

        return {
            "ip": ip,
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "timezone": data.get("timezone"),
        }

    except Exception as e:
        return {"error": str(e)}


def ip_to_location(ip: str, timeout: float = 3.0):
    if not ip or ip == "Unknown":
        return {}
    try:
        r = requests.get(f"https://ipapi.co/{ip}/json/", timeout=timeout)
        data = r.json()
        return {
            "ip": ip,
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
        }
    except:
        return {}
