import yt_dlp
import os
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

url = input("YouTube URL: ").strip()

ydl_opts = {
    "outtmpl": f"{desktop}/%(title)s.%(ext)s",
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"\nİşlem Tamam! Video Masaüstüne kaydedildi.")
except Exception as e:
    print("Hata:", e)