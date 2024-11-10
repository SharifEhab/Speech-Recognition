import json
from yt_extractor import get_audio_url, get_video_infos
from api import save_transcript


def save_video_sentiments(url):
    videos_infos = get_video_infos(url)
    audio_url = get_audio_url(videos_infos)
    title = videos_infos["title"]
    title = title.strip().replace(" ", "_") 

    title = "data/" + title # save the transcript in the data folder

    save_transcript(audio_url, title, sentiment_analysis=True)

    if __name__ == "__main__":
        url = "https://www.youtube.com/watch?v=rz_rus8Vg6Q"
        save_video_sentiments(url)
