import whisper 
import soundfile as sf
#load audio file
audio,sr=sf.read("audio.wav")
text=whisper.transcribe(audio,sr)
print(text)