import streamlit as st
from gtts import gTTS
import tempfile

# Streamlit app title
st.title("Text-to-Audio Converter")

# Text input
user_text = st.text_area("Enter the text you want to convert to speech:")

# Language selection
language = st.selectbox("Select the language for speech:", ["en", "ko", "es", "fr"])

# Generate audio button
if st.button("Generate Audio"):
    if user_text.strip():
        # Convert text to speech using gTTS
        tts = gTTS(text=user_text, lang=language)

        # Save the audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
            tts.save(temp_audio_file.name)
            st.success("Audio generated successfully!")

            # Display the audio player
            st.audio(temp_audio_file.name, format="audio/mp3")
    else:
        st.warning("Please enter some text before generating audio.")
