import youtube_dl
from youtube_dl.utils import DownloadError


ydl = youtube_dl.YoutubeDL()


def get_video_info(url):
    with ydl:
        try:
            result = ydl.extract_info(
                url,
                download=False
            )
        except DownloadError:
            return None

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result
    return video


def get_audio_url(video_info):
    for f in video_info["formats"]:
        # Check for the format you need, e.g., 'audio/mp4'
        if f["ext"] == "m4a":
            return f["url"]

if __name__ == "__main__":
    video_info = get_video_info("https://www.youtube.com/watch?v=rz_rus8Vg6Q")
    audio_url = get_audio_url(video_info)   
    print(audio_url) 