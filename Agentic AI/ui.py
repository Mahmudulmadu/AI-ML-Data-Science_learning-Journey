import streamlit as st
from youtube_analyzer import build_youtube_agent


st.set_page_config(page_title="YouTube Video Analyzer", page_icon="🎥" , layout="centered" )


st.title("YouTube Video Analyzer 🎥")

# cache - fast access, temp storage --> mot freq accessed
@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

# input box
video_url = st.text_input("Enter YouTube video URL:")

button = st.button("Analyze Video") 

if video_url and button:
    with st.spinner("Analyzing video..."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("### Analysis Result:")
    st.markdown(response.content)

        