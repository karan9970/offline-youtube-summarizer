# Offline YouTube Video Summarizer

A fully offline AI pipeline that:

1. Downloads audio from a YouTube video  
2. Converts speech to text using **Whisper-small** (CPU-friendly, offline)  
3. Summarizes the transcript using **TinyLlama** via **Ollama** (offline LLM)  

This project demonstrates an efficient, fully offline ML workflow using open-source models.  
It is suitable for ML/AI engineering assignments, portfolio projects, and production-ready offline summarization systems.

---

## Features

### ✔ Offline Speech-to-Text  
- Powered by **Whisper-small**  
- Works entirely offline  
- Accurate & fast on CPU  

### ✔ Offline Text Summarization  
- Powered by **TinyLlama**  
- Runs via **Ollama**  
- Very fast on CPU  
- Lightweight (fits low-end machines)  

### ✔ Reliable YouTube Audio Download  
- Uses `yt-dlp`  
- Handles all audio formats  
- Generates unique filenames to avoid overwrite issues  

### ✔ Modular, Clean Architecture  
- Each component isolated  
- Easy to replace/extend

