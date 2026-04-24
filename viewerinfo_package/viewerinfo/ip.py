import streamlit as st

def get_ip():
    try:
        headers = st.context.headers

        # Streamlit Cloud / proxies
        ip = headers.get("X-Forwarded-For", "").split(",")[0].strip()

        # Local fallback
        if not ip:
            ip = headers.get("Remote-Addr", "")

        return ip or "Unknown"
    except Exception:
        return "Unknown"
