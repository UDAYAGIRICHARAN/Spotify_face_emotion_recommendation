# Spotify_face_emotion_recommendation
# Emotion-Based Song Player

The Emotion-Based Song Player is a Python application that utilizes computer vision techniques to detect emotions from real-time video stream and plays songs based on the predicted emotions. The application uses a trained deep learning model to classify emotions and fetches song recommendations from the corresponding emotion-specific song lists for both English and Hindi songs.

## Features

- Emotion detection using computer vision techniques.
- Real-time video stream processing.
- English and Hindi song recommendations based on predicted emotions.

## Requirements

- Python 3.7+
- OpenCV
- Pandas
- Keras (with TensorFlow backend)
- Pygame

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/UDAYAGIRICHARAN/Spotify_face_emotion_recommendation.git
   cd Spotify_face_emotion_recommendation
   ```
   
2. Install the required packages using pip:

```
pip install -r requirements.txt


```
## Usage

1. Run the `app.py` script to start the Emotion-Based Song Playe


## python app.py

2. A window will open displaying the real-time video stream from your webcam. The application will detect faces in the video stream and predict the emotion for each face.

3. Based on the predicted emotion, the application will fetch song recommendations from the corresponding emotion-specific song lists.

4. The recommended song will be played using the `pygame` library. Make sure you have an active internet connection to access the song URLs.

5. The application will continue to process the video stream and play songs based on detected emotions until you press 'q' to quit the application.

## Song Data

- The English and Hindi song lists for each emotion are stored in CSV format under the `songs` and `songs1` directories, respectively.

-sportify api will search song and give the result based on song name, Singer name..etc
