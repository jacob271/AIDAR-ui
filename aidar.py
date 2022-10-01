
import requests as requests
import streamlit as st

st.title("AIDAR - Disaster relief management")

image = st.file_uploader("Choose a picture")

if st.button("Style Transfer"):
    if image is not None:
        files = {"file": image.getvalue()}
        res = requests.post("http://127.0.0.1:8000/seg_image", files=files)
        with open("response.jpg", "wb") as f:
            f.write(res.content)
        st.image("response.jpg", width=800)