from flask import Flask, render_template, request
import numpy as np
import librosa
import pandas as pd
import os
import pickle as pk
from tensorflow.keras.models import load_model
import math
from statistics import mode

app = Flask(__name__)
app.config['UPLOADS'] = 'uploads'


# --------------------------------------------------
# Loading The Model, Label Encoder & Recommendations
# --------------------------------------------------
codePath = os.path.dirname(os.path.abspath('app.py'))
le = os.path.join(codePath, 'Models/le.pk')
cnn = os.path.join(codePath, 'Models/best_model.h5')
recom = os.path.join(codePath, 'Models/Final Recs.csv')

le = pk.load(open(le, 'rb'))
model = load_model(cnn)
recs = pd.read_csv(recom)

# -------------------------------------
# Render Main Home Template Index.html
# -------------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# --------------------------------------
# Parameters to Preprocess Data
# --------------------------------------
SAMPLE_RATE = 22050
TRACK_DURATION = 30
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
num_segments = 10
num_mfcc = 13
n_fft = 2048
hop_length = 512


# --------------------------------------
# Preprocesses User Input Taking a File
# --------------------------------------
def getUserInput(path, genre):
  samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
  num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

  user = {"labels": [], "mfcc": []}

  signal, sample_rate = librosa.load(path, sr = SAMPLE_RATE)

  # process all segments of audio file
  for d in range(num_segments):

      # calculate start and finish sample for current segment
      start = samples_per_segment * d
      finish = start + samples_per_segment

      # # extract mfcc
      if len(signal[start : finish]) == samples_per_segment:
        mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc = num_mfcc, 
                                    n_fft = n_fft, hop_length = hop_length)
        mfcc = mfcc.T

        # # store only mfcc feature with expected number of vectors
        if len(mfcc) == num_mfcc_vectors_per_segment:
            user["mfcc"].append(mfcc.tolist())
            user["labels"].append(genre)

  x_user = np.array(user['mfcc'])
  y_user = np.array(user['labels'])
  return x_user, y_user


# --------------------------------------
# Main Function To Process Data and Display Output
# --------------------------------------
@app.route('/', methods = ['POST'])
def upload_files():

    # --------------------------------------
    # Get File From User
    # --------------------------------------
    file = request.files['audiofile']
    filepath = os.path.join(app.config['UPLOADS'], file.filename)
    file.save(filepath)


    # --------------------------------------
    # Preprocess User Input To Put in Model 
    # --------------------------------------
    x_user, y_user = getUserInput(filepath, 'rock')
    x_user = x_user[..., np.newaxis]
    
    
    # ----------------------------
    # Running The Model
    # ----------------------------
    pred = np.argmax(model.predict(x_user), axis = -1)
    genre = le.inverse_transform([mode(pred)])[0]
    
    os.unlink(filepath)


    # ----------------------------
    # Getting The Recommendation
    # ----------------------------
    recommend = recs[recs['Genre'] == genre]

    if recommend.shape[0] >= 3: sample = 3
    else: sample = recommend.shape[0]
    # print('\nSong Recommendations For You Are:')
    df = recommend.sample(sample)


    # ----------------------------
    # Printing The Genre With Recommendations
    # ----------------------------
    dummy = df.to_html(classes = 'data')
    return render_template('index.html', label = genre, 
                           tables=[dummy], titles=df.columns.values)
    # return render_template('index.html', label = genre)

if __name__ == '__main__':
    # bestModel()
    app.run(debug = True)