from flask import Flask, request
from whisper import Transcriber
from pyannote.audio.features import RawAudio
from pyannote.audio.signal import Binarize
from pyannote.audio.labeling.extraction import SequenceLabeling
import pyaudio
import wave
import struct

app = Flask(__name__)

# Initialize the transcriber and the speaker labeler
transcriber = Transcriber()
raw_audio = RawAudio(sample_rate=16000)
binarize = Binarize(offset=0.5, onset=0.5, log_scale=True, min_duration_off=0.1, min_duration_on=0.1)
labeler = SequenceLabeling(binarize)

# Define the endpoint for receiving live audio streams
@app.route('/live_transcription', methods=['POST'])
def live_transcription():
    # Get the audio data from the request
    data = request.data
    
    # Convert the binary data to an array of short integers
    samples = struct.unpack(f'<{len(data)//2}h', data)
    
    # Transcribe the audio using Whisper
    text = transcriber.transcribe(samples)
    
    # Generate speaker labels using Pyannote
    signal = raw_audio(samples)
    labels = labeler(signal)
    speaker_labels = []
    for segment, label in labels.itertracks(label=True):
        speaker_labels.append({'start': segment.start, 'end': segment.end, 'label': label})
    
    # Return the transcription and speaker labels as JSON
    return {'transcription': text, 'speaker_labels': speaker_labels}

if __name__ == '__main__':
    # Initialize the Pyaudio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    
    # Start the Flask app
    app.run()
    
    # Stop the Pyaudio stream when the app is closed
    stream.stop_stream()
    stream.close()
    p.terminate()
