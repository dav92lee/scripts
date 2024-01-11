import sys
from pytube import YouTube

# Check if a URL is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python download-yt.py <URL>")
    sys.exit(1)

# The first command-line argument is the URL
url = ''.join(sys.argv[1:])

try:
    yt = YouTube(url)
    yt.streams.filter().get_highest_resolution().download()
    print(f"Finished downloading: {yt.title}")
except Exception as e:
    print(f"An error occurred: {e}")