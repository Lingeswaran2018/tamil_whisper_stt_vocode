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
venv\Scripts\activate 

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
```
## File Structure
``` bash
tamil_vocode/
├── vocode-python/                 
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
├── .gitignore                     
└── README.md  


