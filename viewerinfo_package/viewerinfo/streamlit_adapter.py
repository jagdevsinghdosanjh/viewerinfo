from .ip import get_ip
from .device import get_device
from .geo import get_geo

def get_streamlit_viewer():
    return {
        "ip": get_ip(),
        "device": get_device(),
        "geo": get_geo()
    }
