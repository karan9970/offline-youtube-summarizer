from downloader import download_audio
from transcriber import transcribe
from summarizer import ollama_summarize

def process_video(url):
    print("\nDownloading audio...")
    audio_file = download_audio(url)

    print("\nTranscribing using Whisper-small...")
    transcript = transcribe(audio_file)

    print("\nSummarizing using TinyLlama (offline via Ollama)...")
    summary = ollama_summarize(transcript, model="tinyllama")

    print("\n=== FINAL SUMMARY ===\n")
    print(summary)

    return summary


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    process_video(url)
