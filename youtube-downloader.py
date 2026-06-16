from yt_dlp import YoutubeDL

url = input("Enter YouTube Video URL:")

# download options
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
}

# download video
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")
