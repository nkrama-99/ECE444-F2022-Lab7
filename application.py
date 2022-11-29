from flask import Flask
from flask import request
from flask import jsonify
from sklearn. feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# >>>>>>>>>>>> Model Setup
# Load and prepare model to be used for predictions
loaded_model = None
with open('basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)

vectorizer = None
with open('count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle. load(vd)

# Predict identifies if input is fake news or real news 
def predict(input):
    prediction = loaded_model.predict(vectorizer.transform([input]))[0]
    return prediction

# >>>>>>>>>>>> Flask Setup
application = Flask(__name__)

# predict endpoint to receive prediction
@application.route('/predict', methods=['POST'])
def predictions():
    content = request.json
    input = content['text']
    prediction = predict(input)
    return jsonify(prediction=prediction)

# index page for aws health checks
header_text = '''<html>\n<head> <title>EB Flask Test</title> </head>\n</html>'''
application.add_url_rule('/', 'index', (lambda: header_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()