from flask import Flask, render_template, request
# from flask_ngrok import run_with_ngrok
import os

app = Flask(__name__)
# run_with_ngrok(app)

app.config['UPLOADS'] = 'uploads'

# def bestModel():
#     global mymodel
#     mymodel = load_model('catDog.h5')

@app.route('/')
def home():
    return render_template('index.html')

# def predicting(file):
#   # img = load_img(file, grayscale = True, target_size = (28, 28, 1), color_mode = 'grayscale')
#   # img = img_to_array(img)
#     img = cv2.imread(file)
#   #   img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img = cv2.resize(img, (32, 32))
#     img = np.resize(img, (1, 32, 32, 3)) / 255
#     pred = mymodel.predict(img)
#     if pred > 0.5: return 'dog'
#     else: return 'cat'

@app.route('/', methods = ['POST'])
def upload_files():
    file = request.files['audiofile']
    filepath = os.path.join(app.config['UPLOADS'], file.filename)
    file.save(filepath)
    # pred = predicting(filepath)
    return render_template('index.html', label = 'why this kolaveri d')

if __name__ == '__main__':
    # bestModel()
    app.run(debug = True)