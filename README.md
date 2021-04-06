Title: Music Genre Detection and Recommendation.

Authors: Mithesh R, Arth A, Heetansh J, Ayaan K.

Under the guidance of: Pranav N.

Date: 5-April-2021

# Music Genre Detection and Recommendation.

## About the Project:
Music is an essential unwinding for most of us. With new songs added to music streaming platforms like Spotify, Amazon Prime Music, JioSaavn every week, music listeners want to keep their playlist updated. With this project we aim to provide a similar experience with regards to music recommendation for those who use the aforementioned applications and to those who don’t. 
The aim of this project is to classify the genre of songs, mainly into: Pop, Rock, Hip-Hop, Reggae, Country, Disco, Classical, Jazz with the help of an application built on Flask. Along with the genre, users of the application get recommended with upto three songs similar to the one searched for.
Key features:
- Easy to use interface
- Smaller application size
- Accurate genre predictions
- Recommendations to help build your playlist for an enthralling musical experience

### Disclaimer:
- The app supports the use of .WAV file format. Please use the link in the application to convert to .WAV format from .MP3 or .MPEG formats.

### Dependencies:
We use the following python libraries:
* [numpy]
* [os]
* [sklearn]
* [pandas]
* [librosa]
* [pickle]
* [tensorflow]
* [statistics]
* [math]
* [keras]
* [flask]

### Run the application:

- Download the application files from this repo as a zip file

- Unzip the contents

- Open the Command prompt/ Terminal/ Windows Powershell and cd to the folder’s directory

- Ensure python v.3 is running on your system.

- For windows:

— - Type the following in : Command prompt/ Windows Powershell

- --

```sh
set FLASK_APP = app.py
```
— -- 

 ```sh
set FLASK_DEBUG = 1
```
— -- 

```sh
flask run
```
— -- 

— Type the ‘localhost’ url displayed on your command line prompt in your browser.

- For MacOS/ Linux:
— - Type the following in Terminal”

```sh
 python -3 ./app.py
 ```
—Type the ‘localhost’ url displayed on your terminal in your browser.

### Working Demo

- The website will look as shown below. Press the red button to upload a song file of your choice in .wav formt. If you have the music file in any other format, there is a link provided below the button to convert the any type of audio file to a .wav file.
![Input Image](https://github.com/FlintyTub49/MusicRecommender/blob/main/Output/input.png)

- After processing (which might take upto 30 seconds depending on the file size) you will receive the output as follows. The website will tell you a genre for your uploaded file and on the basis of that recommend you songs of the same genre. The list of all songs available for recommendations along with their genre is given in the Models folder as a .csv file.
![Output Image](https://github.com/FlintyTub49/MusicRecommender/blob/main/Output/output.png)

### Development

Developed By :-
[Mithesh R], 
[Arth Akhouri],
[Heetansh Jhaveri],
[Ayaan Khan]


[//]: #
	[numPy]: <https://numpy.org>
	[pandas]: <https://pandas.pydata.org>
	[sklearn]: <https://scikit-learn.org/stable/>
	[os]: <https://docs.python.org/3/library/os.html>
	[librosa]: <https://pandas.pydata.org>
	[pickle]: <https://docs.python.org/3/library/pickle.html>
	[os]: <https://docs.python.org/3/library/os.html>
	[librosa]: <https://librosa.org/doc/latest/index.html>
	[tensorflow]: <https://www.tensorflow.org>
	[statistics]: <https://docs.python.org/3/library/statistics.html>
	[math]: <https://docs.python.org/3/library/math.html>
	[keras]: <https://keras.io>
	[flask]: <https://flask.palletsprojects.com/en/1.1.x/>
	[Arth Akhouri]: <https://github.com/user/FlintyTub49>
	[Mithesh R]: <https://github.com/user/259-mit>
	[Heetansh Jhaveri]: <https://github.com/user/hjj31>
	[Ayaan Khan]: <https://github.com/user/ayaan-27>
