import whisper
import soundfile as sf
audio,sr=sf.read("audio.mp3")
text=whisper.transcribe(audio,sr)
print(text)