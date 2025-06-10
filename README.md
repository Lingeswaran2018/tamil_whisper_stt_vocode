# Tamil Whisper STT Transcription API

This project integrates a fine-tuned Hugging Face Whisper model for Tamil with FastAPI, using Vocode-style structure for modularity.

## Features

- Upload `.wav` files and get Tamil transcriptions
- Uses Hugging Face `WhisperForConditionalGeneration`
- Fully local (no external STT APIs required)

## How to Run

```bash
# Set up virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r app/requirements.txt

# Run the app
uvicorn app.main:app --reload


File Structure
tamil_vocode/
├── vocode-python/                 ✅ (only your changes inside `vocode/`)
│   └── vocode/
│       └── streaming/
│           ├── transcriber/
│           │   ├── base_transcriber.py
│           │   └── tamil_whisper_transcriber.py
│           └── models/
│               └── transcriber.py
├── app/
│   ├── main.py
│   └── requirements.txt
├── .gitignore                     ✅ (see below)
└── README.md                      ✅ (brief description of what it does)
