import streamlit as st
import pandas as pd
from pathlib import Path
from viewerinfo.streamlit_adapter import get_streamlit_viewer

LOG_PATH = Path(__file__).parent / "logs" / "viewer_log.csv"
LOG_PATH.parent.mkdir(exist_ok=True)

def log_viewer(viewer: dict):
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

def main():
    st.title("Viewer Analytics Dashboard")

    # 1. Capture current viewer
    viewer = get_streamlit_viewer()
    st.subheader("Current viewer")
    st.json(viewer)

    # 2. Log it
    log_viewer(viewer)

    # 3. Load all data
    data = load_data()
    if data.empty:
        st.info("No data logged yet.")
        return

    # 4. Filters
    st.sidebar.header("Filters")
    country = st.sidebar.multiselect(
        "Country", sorted(data["country"].dropna().unique().tolist())
    )
    browser = st.sidebar.multiselect(
        "Browser", sorted(data["browser"].dropna().unique().tolist())
    )

    filtered = data.copy()
    if country:
        filtered = filtered[filtered["country"].isin(country)]
    if browser:
        filtered = filtered[filtered["browser"].isin(browser)]

    st.subheader("Aggregated stats")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total views", len(filtered))
        st.write("By browser")
        st.bar_chart(filtered["browser"].value_counts())
    with col2:
        st.write("By OS")
        st.bar_chart(filtered["os"].value_counts())

    st.subheader("Raw data")
    st.dataframe(filtered)

if __name__ == "__main__":
    main()
