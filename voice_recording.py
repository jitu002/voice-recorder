from curses import KEY_BACKSPACE
from tkinter import TRUE
import wave
import pyaudio
import keyboard

frames_per_buffer=1024
format=pyaudio.paInt16
rate=44100

p=pyaudio.PyAudio()
print("start recording")
stream=p.open(format=format,channels=2,rate=rate,frames_per_buffer=frames_per_buffer,input=True)


frames=[]
try:
    while True:
        data=stream.read(frames_per_buffer)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()

## saving the audio file

obj=wave.open("python programming\output.m4a","wb")
obj.setnchannels(2)
obj.setsampwidth(p.get_sample_size(format))
obj.setframerate(rate)
obj.writeframes(b"".join(frames))
obj.close()