# Gesture Genie

## Overview

Gesture Genie is a web application that bridges the gap between the deaf and hearing communities by translating spoken language into American Sign Language (ASL) using real-time video and tone detection. Additionally, the application offers sign-to-speech functionality, translating ASL gestures into spoken language using computer vision techniques.

## Features

- **Real-time ASL Translation:** Converts recorded audio into ASL videos.
- **Tone Detection:** Analyzes the tone of the speaker and changes the background color accordingly:
  - Red: Angry
  - Blue: Sad
  - Yellow: Happy
  - Green: Neutral
- **Sign-to-Speech Translation:** Uses computer vision to detect and interpret ASL gestures, translating them into spoken language.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- Requests
- BeautifulSoup4
- pydub
- Hume API access
- MediaPipe
- OpenCV

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/bdonyan/GestureGenie.git
    cd GestureGenie
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Hume API key and OpenAI API key in the `flask_server.py` file:
    ```python
    HUME_API_KEY = 'your_hume_api_key'
    OPENAI_API_KEY = 'your_openai_api_key'
    ```

### Running the Application

1. Start the Flask server:
    ```bash
    python flask_server.py
    ```

2. Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the application.

## Usage

### Speech to Sign

1. On the homepage, click on "Try Now" to start recording.
2. Click "Start Recording" to record your audio.
3. Click "Stop Recording" to stop and upload the audio.
4. The application will process the audio, translate it to ASL, and display the corresponding ASL video. The background color will change based on the tone detected.

### Sign to Speech

1. Navigate to the "Sign to Speech" section of the application.
2. Ensure your webcam is connected and click "Start Detection".
3. Perform ASL gestures in front of the camera.
4. The application will detect and interpret the gestures, translating them into spoken language which will be displayed on the screen.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.
