import requests as requests
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="🛰", layout='wide')

st.markdown("# AIDAR 🛰 - Disaster Management System")
st.sidebar.markdown("# AIDAR 🛰")

st.subheader("Damage Assessment via Satellite imagery")

image = st.file_uploader("Upload a picture")

if st.button("Get Damage Assessment"):
    if image is not None:
        files = {"file": image.getvalue()}
        res = requests.post("http://127.0.0.1:8000/segment_image", files=files)
        with open("response.jpg", "wb") as f:
            f.write(res.content)
        st.image("response.jpg", width=800)