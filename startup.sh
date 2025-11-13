
#!/bin/bash

# To run locally, you can set the PORT environment variable (default is 8501):
# export PORT=8501

# If ffmpeg is not installed, add installation steps here.
streamlit run whisper_app.py --server.port=$PORT --server.enableCORS=false
