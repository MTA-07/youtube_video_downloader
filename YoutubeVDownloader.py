import yt_dlp

url = input("YouTube URL: ").strip()

ydl_opts = {
    "outtmpl": "%(title)s.%(ext)s",
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Video indirildi!")
except Exception as e:
    print("Hata:", e)