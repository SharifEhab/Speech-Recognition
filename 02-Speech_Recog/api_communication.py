
import requests
import time
from api_secret import API_KEY_ASSEMBLYAI 

upload_endpoint = "https://api.assemblyai.com/v2/upload" # endpoint for uploading the file

transcript_endpoint = "https://api.assemblyai.com/v2/transcript" # endpoint for getting the transcript
headers = { 'authorization': API_KEY_ASSEMBLYAI  }

# read the file in chunks, 5MB at a time
def upload(filename):
    def read_file(file_name, chunk_size=5242880):
        with open(file_name, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data


    # post request to the server
    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))    


    audio_url = upload_response.json()['upload_url'] # get the audio url from the response
    return audio_url

# transcribe

def transcribe(audio_url):
    transcript_request = { "audio_url" : audio_url } # audio url from the response

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    transcript_id = transcript_response.json()['id'] # get the job id from the response
    return transcript_id 





# poll, is the transcript ready? 
def poll(transcript_id): 
    polling_endpoint = transcript_endpoint + '/' + transcript_id # endpoint for polling the status of the transcript, is it ready?
    polling_response = requests.get(polling_endpoint, headers=headers) # get the status of the transcript

    return polling_response.json()

def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data,data['error']
        
        print('Waiting for 30 seconds..')
        time.sleep(30)  # wait for 30 seconds before polling again
        



  


# save transcript
def save_transcript(audio_url,filename):
    data, error = get_transcription_result_url(audio_url) # get the transcript id and the status of the transcript

    if data :
        text_filename = filename + ".txt" 
        with open(text_filename, "w") as f:
            f.write(data['text']) # write the transcript to a text file
        print('Transcription saved!!')  

    elif error:
        print("Error!! ", error)
