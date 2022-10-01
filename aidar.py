import requests as requests
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="🛰", layout='wide')

st.markdown("# AIDAR 🛰 - Disaster Relief System")
st.sidebar.markdown("# AIDAR 🛰")

st.subheader("Damage Assessment via Satellite imagery")
column1, column2 = st.columns(2)

with column1:
    image = st.file_uploader("Upload a picture")

    if st.button("Get Damage Assessment"):
        if image is not None:
            files = {"file": image.getvalue()}
            res = requests.post("http://127.0.0.1:8000/seg_image", files=files)
            with open("response.jpg", "wb") as f:
                f.write(res.content)
            st.image("response.jpg", width=800)

with column2:
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)
