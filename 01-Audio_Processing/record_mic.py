import pyaudio
import wave


FRAMES_PER_BUFFER = 3200 # number of frames per buffer
FORMAT = pyaudio.paInt16 # 16 bit integer format
CHANNELS = 1 # 1 channel
RATE = 16000 # 16 kHz sampling rate

P = pyaudio.PyAudio() # create an interface to PortAudio, object P is a PortAudio system object

stream = P.open(format=FORMAT, 
                channels=CHANNELS,
                  rate=RATE, 
                  input=True, 
                  frames_per_buffer=FRAMES_PER_BUFFER) # open the stream



print("start recording")

seconds = 5 # duration of recording in seconds
frames=[]
for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    data = stream.read(FRAMES_PER_BUFFER) # read the frames from the stream
    frames.append(data) # append all the frames to the list

stream.stop_stream() # stop recording
stream.close() # close the stream
P.terminate() # terminate the PortAudio interface    

obj = wave.open("output.wav","wb") # create a wave object
obj.setnchannels(CHANNELS) # set the number of channels
obj.setsampwidth(P.get_sample_size(FORMAT)) # set the sample width
obj.setframerate(RATE) # set the frame rate 
obj.writeframes(b"".join(frames)) # write the frames to the file , b"" is for binary data
obj.close() # close the wave object   