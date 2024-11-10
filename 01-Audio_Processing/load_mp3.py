from pydub import AudioSegment # manipulate audio files

#AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe" # path to ffmpeg.exe    

audio = AudioSegment.from_wav("output.wav") # read the audio file

 
#increase volume by 10 dB
audio = audio + 1500 


audio = audio * 1 # repeat the audio file 1 times

audio = audio.fade_in(2000) # fade in the audio file in 2000 milliseconds

audio.export("output.mp3", format="mp3") # export the audio file to mp3 format

audio2 = AudioSegment.from_mp3("output.mp3") # read the audio file

print("done")

