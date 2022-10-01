import requests as requests
import streamlit as st

st.title("AIDAR - Disaster Management")

st.subheader("Upload a satellite image to receive damage assessment")
image = st.file_uploader("Upload a picture")

if st.button("Get Damage Assessment"):
    if image is not None:
        files = {"file": image.getvalue()}
        res = requests.post("http://127.0.0.1:8000/seg_image", files=files)
        with open("response.jpg", "wb") as f:
            f.write(res.content)
        st.image("response.jpg", width=800)

# display a divider between the two widgets

