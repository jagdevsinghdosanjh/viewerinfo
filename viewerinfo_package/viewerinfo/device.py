from user_agents import parse as parse_ua
import streamlit as st

def get_device():
    # Get user-agent from Streamlit request headers
    ua_string = st.context.headers.get("User-Agent", "")
    ua = parse_ua(ua_string)

    return {
        "browser": ua.browser.family,
        "browser_version": ua.browser.version_string,
        "os": ua.os.family,
        "os_version": ua.os.version_string,
        "device": ua.device.family,
        "is_mobile": ua.is_mobile,
        "is_tablet": ua.is_tablet,
        "is_pc": ua.is_pc,
    }


def get_device_info(user_agent: str):
    if not user_agent:
        return {}
    ua = parse_ua(user_agent)
    return {
        "browser": ua.browser.family,
        "browser_version": ua.browser.version_string,
        "os": ua.os.family,
        "os_version": ua.os.version_string,
        "device": ua.device.family,
        "is_mobile": ua.is_mobile,
        "is_tablet": ua.is_tablet,
        "is_pc": ua.is_pc,
    }
