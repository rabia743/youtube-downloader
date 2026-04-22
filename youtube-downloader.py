from yt_dlp import YoutubeDL

url = input("Enter YouTube Video URL: https://youtu.be/VXtjG_GzO7Q?si=0vORTSRfKv-8FfG-")

# download options
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
}

# download video
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")