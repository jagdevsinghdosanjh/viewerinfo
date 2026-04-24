import streamlit as st
from viewerinfo.streamlit_adapter import get_streamlit_viewer

viewer = get_streamlit_viewer()
st.write(viewer)
