"""
Audio file formats
.mp3 ---> lossy compression (some data loss) fourier transform  (not perfectly reconstructs the original audio)
.flac ---> lossless compression (perfectly reconstructs the original audio)
.wav ---> uncompressed (no data loss) large file size,  standard format for audio processing

"""
import wave

# Audio signal parameters
# number of channels (1 for mono, 2 for stereo)
# sample width in bytes (1 for 8 bits, 2 for 16 bits, 4 for 32 bits)
# sampling rate in samples per second (commonly 44100 Hz)
# number of frames (total number of samples)
# values of frames (sequence of samples), binary data

obj = wave.open("wave_example.wav","rb")

print("Number of channels: ", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate() # total time of audio in seconds
print("total time of audio in seconds", t_audio) 

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

obj.close()

obj_new = wave.open("wave_example_new.wav","wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(30000)

obj_new.writeframes(frames) # duplicate the audio file , write the frames to the new file
 
obj.close()



