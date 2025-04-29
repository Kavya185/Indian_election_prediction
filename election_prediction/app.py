# app.py

import streamlit as st
from config import NATIONAL_PARTIES, STATE_PARTIES
from utils import get_party_support, get_sorted_support

st.title("🗳️ Indian Election Sentiment Prediction Dashboard")

view = st.radio("Select View", ["General (National)", "State-wise"])

if view == "General (National)":
    st.subheader("🇮🇳 General Election Sentiment")
    results = get_party_support(NATIONAL_PARTIES)
    sorted_results = get_sorted_support(results)
    
    for party, sentiment in sorted_results:
        st.markdown(f"**{party}** - Support Score: `{sentiment['support_score']:.2f}`")
        st.progress((sentiment['support_score'] + 1) / 2)

else:
    state = st.selectbox("Choose a state", list(STATE_PARTIES.keys()))
    st.subheader(f"📍 State-wise Election Sentiment - {state}")
    state_parties = STATE_PARTIES[state]
    results = get_party_support(state_parties, state)
    sorted_results = get_sorted_support(results)

    for party, sentiment in sorted_results:
        st.markdown(f"**{party}** - Support Score: `{sentiment['support_score']:.2f}`")
        st.progress((sentiment['support_score'] + 1) / 2)
