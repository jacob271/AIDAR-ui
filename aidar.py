
import requests as requests
import streamlit as st

import openai_api

st.title("AIDAR - Disaster relief management")

st.subheader("Damage Assessment")
image = st.file_uploader("Choose a picture")

if st.button("Get Damage Assessment"):
    if image is not None:
        files = {"file": image.getvalue()}
        res = requests.post("http://127.0.0.1:8000/seg_image", files=files)
        with open("response.jpg", "wb") as f:
            f.write(res.content)
        st.image("response.jpg", width=800)

# display a divider between the two widgets
st.markdown("---")

st.subheader("Recommendations")

# display a text box to enter the scenario

scenario_text = st.text_input("Enter a description of the situation. Include the type of disaster, location (city, "
                              "state etc.) of impact, affected number of people and other data.")

# display quote before the field
st.write("Example: Flooded village in Vietnam. The population of the village is around 13500 people. There are "
         "several power outages and risks of water contamination throughout the whole area.")


if st.button("Get Tasks"):
    if scenario_text is not None:
        res = openai_api.get_tasks_from_the_scenario(scenario_text)
        st.write(res)

