
import streamlit as st
import whisper
import tempfile
import os

# Whisper Speech-to-Text App
st.title("🎙 Whisper Speech-to-Text App")

# Model selection
model_size = st.selectbox(
    "Select model size (balance between speed and accuracy)",
    ["tiny", "base", "small", "medium", "large"]
)
st.caption("Larger models are more accurate but may take longer to process.")

# Audio file upload
uploaded_file = st.file_uploader(
    "Upload an audio file (mp3, wav, m4a, webm)",
    type=["mp3", "wav", "m4a", "webm"]
)

if uploaded_file is not None:
    # Save to a temporary file
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name
    except Exception as e:
        st.error(f"Error saving uploaded file: {e}")
        temp_path = None

    if temp_path:
        st.audio(uploaded_file, format='audio/wav')

        if st.button("Start Transcription"):
            with st.spinner("Transcribing..."):
                try:
                    model = whisper.load_model(model_size)
                    result = model.transcribe(temp_path)
                    st.success("Transcription completed!")
                    st.text_area("📝 Transcription Result", value=result["text"], height=300)
                except Exception as e:
                    st.error(f"Transcription failed: {e}")
            # Delete the temporary file
            try:
                os.remove(temp_path)
            except Exception as e:
                st.warning(f"Could not delete temp file: {e}")
