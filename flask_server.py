from flask import Flask, request, render_template, jsonify
import whisper
import os

app = Flask(__name__)

model = whisper.load_model("base")

@app.route('/')
def index():
    return render_template('record_audio.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        file_path = os.path.join('/tmp', file.filename)
        file.save(file_path)
        text = transcribe_audio(file_path)
        return jsonify({"transcribed_text": text})

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
