import yt_dlp
import uuid

def download_audio(url):
    # unique filename to avoid overwrite
    output_name = f"audio_{uuid.uuid4().hex}.mp3"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_name.replace(".mp3", ".%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_name
