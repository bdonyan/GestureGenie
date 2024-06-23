from flask import Flask, request, render_template, jsonify
from pydub import AudioSegment
import requests
import os
import string
from bs4 import BeautifulSoup

app = Flask(__name__)

OPENAI_API_KEY = ''

def transcribe_audio(file_path):
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }
    data = {
        'model': 'whisper-1',
        'response_format': 'json'
    }
    files = {
        'file': open(file_path, 'rb')
    }
    response = requests.post('https://api.openai.com/v1/audio/transcriptions', headers=headers, data=data, files=files)
    response_json = response.json()
    if 'text' in response_json:
        return response_json['text']
    else:
        return response_json  # Return the entire response if 'text' is not found for debugging

@app.route('/')
def index():
    return render_template('record_audio.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Convert webm to wav if necessary
        if file_path.endswith('.webm'):
            audio = AudioSegment.from_file(file_path, format='webm')
            wav_path = file_path.replace('.webm', '.wav')
            audio.export(wav_path, format='wav')
        else:
            wav_path = file_path
        
        text = transcribe_audio(wav_path)
        words = preprocess_text(text)
        video_urls = []
        for word in words:
            video_url = get_sign_video_url(word)
            if not video_url:
                # For fingerspelling, get each letter's URL
                for letter in word:
                    letter_url = get_sign_video_url(letter)
                    if letter_url:
                        video_urls.append({"word": f"{word} ({letter})", "url": letter_url})
            else:
                video_urls.append({"word": word, "url": video_url})
        
        return jsonify({"video_urls": video_urls})

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def get_sign_video_url(word):
    search_url = f"https://www.signingsavvy.com/search/{word}"
    response = requests.get(search_url)
    print(f"Searching for {word} at {search_url}")  # Debugging statement
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        source_tag = soup.find('source', {'type': 'video/mp4'})
        if source_tag:
            video_url = source_tag['src']
            print(f"Found video URL for {word}: {video_url}")  # Debugging statement
            return video_url
        search_results = soup.find('div', class_='search_results')
        if search_results:
            first_link = search_results.find('a')
            if first_link:
                link_url = f"https://www.signingsavvy.com/{first_link['href']}"
                sub_response = requests.get(link_url)
                print(f"Accessing first link for {word} at {link_url}")  # Debugging statement
                if sub_response.status_code == 200:
                    sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                    source_tag = sub_soup.find('source', {'type': 'video/mp4'})
                    if source_tag:
                        video_url = source_tag['src']
                        print(f"Found video URL for {word}: {video_url}")  # Debugging statement
                        return video_url
    return None

if not os.path.exists('uploads'):
    os.makedirs('uploads')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
