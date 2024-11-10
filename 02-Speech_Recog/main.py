
#from api_secrets import API_KEY_ASSEMBLEYAI
from api_communication import * 
import sys
#upload



filename = sys.argv[1]  # get the filename from the command line



audio_url = upload(filename) # upload the file and get the audio url

save_transcript(audio_url,filename) # save the transcript to a text file