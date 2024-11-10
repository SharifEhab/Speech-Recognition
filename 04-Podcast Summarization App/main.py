from api_communication import *
import streamlit as st
import json


st.title('Podcast Summarization App')
episode_id = st.sidebar.text_input('Please enter the podcast episode ID:')
button = st.sidebar.button('Get podast summary', on_click=save_transcript, args = (episode_id,) )   

def get_clean_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_t = f'{minutes:02d}:{seconds:02d}'
        
    return start_t

if button:
    filename = episode_id + '_chapters.json'

    with open(filename, 'r') as f:
        data = json.load(f)
        chapters = data['chapters']
        podcast_title = data['podcast_title']
        episode_title = data['episode_title']
        thumbnail = data['episode_thumbnail']


    st.header(f'{podcast_title}: {episode_title}')
    st.image(thumbnail)

    for chapter in chapters:
        with st.expander(chapter['gist']) + '_' + get_clean_time(chapter['start']):
            chapter['summary']
   # save_transcript('1e2f4e1e1a21441c8a90b946eddc33fc')