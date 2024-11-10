import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("wave_example.wav","rb")


sample_freq = obj.getframerate() # sampling rate in samples per second (commonly 44100 Hz)
n_samples = obj.getnframes() # number of frames (total number of samples)
signal_wave = obj.readframes(-1) # values of frames (sequence of samples), binary data

obj.close()


t_audio = n_samples / sample_freq # total time of audio in seconds

print(t_audio)

# convert binary data to integers
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0,t_audio,num=len(signal_array) )

print(len(times), len(signal_array))

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Audio signal")   
plt.xlabel("Time (s)")
plt.ylabel("Audio Signal")  
plt.xlim(0,t_audio)
plt.show()