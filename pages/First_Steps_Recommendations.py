import streamlit as st
import openai_api


st.set_page_config(page_icon="📋", layout='wide')

st.markdown("# First steps recommendations")
st.sidebar.markdown("# Guidance System 📋")


scenario_text = st.text_input("Enter a description of the situation. Include the type of disaster, location (city, "
                              "state etc.) of impact, affected number of people and other data.")

st.write("Example: Flooded village in Vietnam. The population of the village is around 13500 people. There are "
         "several power outages and risks of water contamination throughout the whole area.")

if scenario_text is not None and scenario_text != "":
    res = openai_api.get_tasks_from_the_scenario(scenario_text)

    tabs = st.tabs([f"Suggestion {i}" for i in range(1, len(res) + 1)])
    for i in range(len(res)):
        tabs[i].write(res[i])
