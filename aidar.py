from io import StringIO

import pandas as pd
import requests as requests
import streamlit as st

from PIL import Image


st.title("AIDAR - Disaster relief management")

image = st.file_uploader("Choose a picture")

if st.button("Style Transfer"):
    if image is not None:
        files = {"file": image.getvalue()}
        res = requests.post("http://127.0.0.1:8000/seg_image", files=files)
        with open("response.jpg", "wb") as f:
            f.write(res.content)
        st.image("response.jpg", width=800)
        #st.image(image, width=500)

#if image is not None:
    # To read file as bytes:
#    bytes_data = image.getvalue()
#    st.write(bytes_data)

    # To convert to a string based IO:
#    stringio = StringIO(image.getvalue().decode("utf-8"))
#    st.write(stringio)

    # To read file as string:
#    string_data = stringio.read()
#    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
#    dataframe = pd.read_csv(image)
#    st.write(dataframe)
