from flask import Flask,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector App")

@app.route('/emotionDetector')
def get_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] == "None":
        return(" Invalid text! Please try again!.", 400)
    return result

if __name__ == "__main__":
    app.run(debug=True)
