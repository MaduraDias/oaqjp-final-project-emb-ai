from flask import Flask,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector App")

@app.route('/emotionDetector')
def get_emotion():
    textToAnalyze = request.args.get('textToAnalyze')
    result = emotion_detector(textToAnalyze)
    return (result)
    

if __name__ == "__main__":
    app.run(debug=True)