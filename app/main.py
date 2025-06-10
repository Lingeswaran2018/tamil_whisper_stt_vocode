from fastapi import FastAPI, UploadFile, File
import uuid
import shutil
import os
from vocode.streaming.transcriber.tamil_whisper_transcriber import (
    TamilWhisperTranscriber, TamilWhisperTranscriberConfig
)

app = FastAPI()
transcriber = TamilWhisperTranscriber(TamilWhisperTranscriberConfig())

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        temp_filename = f"temp_{uuid.uuid4()}.wav"
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        with open(temp_filename, "rb") as f:
            audio_bytes = f.read()

        result = await transcriber.transcribe(audio_bytes)
        os.remove(temp_filename)

        return {"transcription": result.message}
    
    except Exception as e:
        return {"error": str(e)}
