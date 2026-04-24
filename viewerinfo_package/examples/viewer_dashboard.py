import streamlit as st
import pandas as pd
from pathlib import Path
from viewerinfo.streamlit_adapter import get_streamlit_viewer

LOG_PATH = Path(__file__).parent / "logs" / "viewer_log.csv"
LOG_PATH.parent.mkdir(exist_ok=True)

# -----------------------------
# Logging
# -----------------------------
def log_viewer(viewer):
    row = {
        "ip": viewer.get("ip"),
        "browser": viewer["device"].get("browser"),
        "browser_version": viewer["device"].get("browser_version"),
        "os": viewer["device"].get("os"),
        "os_version": viewer["device"].get("os_version"),
        "device": viewer["device"].get("device"),
        "is_mobile": viewer["device"].get("is_mobile"),
        "is_tablet": viewer["device"].get("is_tablet"),
        "is_pc": viewer["device"].get("is_pc"),
        "geo_error": viewer["geo"].get("error"),
        "city": viewer["geo"].get("city"),
        "region": viewer["geo"].get("region"),
        "country": viewer["geo"].get("country"),
        "latitude": viewer["geo"].get("latitude"),
        "longitude": viewer["geo"].get("longitude"),
    }

    df = pd.DataFrame([row])
    if LOG_PATH.exists():
        df.to_csv(LOG_PATH, mode="a", header=False, index=False)
    else:
        df.to_csv(LOG_PATH, index=False)

def load_data():
    if LOG_PATH.exists():
        return pd.read_csv(LOG_PATH)
    return pd.DataFrame()

# -----------------------------
# Dashboard
# -----------------------------
def main():
    st.title("📊 Viewer Analytics Dashboard")

    # Capture viewer
    viewer = get_streamlit_viewer()
    st.subheader("Current Viewer")
    st.json(viewer)

    # Log viewer
    log_viewer(viewer)

    # Load all data
    data = load_data()
    if data.empty:
        st.info("No viewer data yet.")
        return

    st.subheader("Dataset")
    st.dataframe(data)

    # -----------------------------
    # Filters
    # -----------------------------
    st.sidebar.header("Filters")

    browser_filter = st.sidebar.multiselect(
        "Browser", sorted(data["browser"].dropna().unique())
    )
    os_filter = st.sidebar.multiselect(
        "Operating System", sorted(data["os"].dropna().unique())
    )

    filtered = data.copy()
    if browser_filter:
        filtered = filtered[filtered["browser"].isin(browser_filter)]
    if os_filter:
        filtered = filtered[filtered["os"].isin(os_filter)]

    # -----------------------------
    # Metrics
    # -----------------------------
    st.subheader("Summary Metrics")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Views", len(filtered))
    col2.metric("Unique Browsers", filtered["browser"].nunique())
    col3.metric("Unique OS", filtered["os"].nunique())

    # -----------------------------
    # Charts
    # -----------------------------
    st.subheader("Browser Distribution")
    st.bar_chart(filtered["browser"].value_counts())

    st.subheader("OS Distribution")
    st.bar_chart(filtered["os"].value_counts())

    st.subheader("Device Type")
    device_counts = {
        "PC": filtered["is_pc"].sum(),
        "Mobile": filtered["is_mobile"].sum(),
        "Tablet": filtered["is_tablet"].sum(),
    }
    st.bar_chart(device_counts)

    # -----------------------------
    # Geo (will work once deployed)
    # -----------------------------
    st.subheader("Country Distribution (when deployed)")
    if "country" in filtered.columns:
        st.bar_chart(filtered["country"].value_counts())

if __name__ == "__main__":
    main()
