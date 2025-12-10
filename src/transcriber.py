import whisper

# load whisper model only once
model = whisper.load_model("small")

def transcribe(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
