"""
This module creates a Flask web application for detecting emotions in text.
It provides an endpoint `/emotionDetector` for analyzing the emotion of the given text.
"""

from flask import Flask,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector App")

@app.route('/emotionDetector')
def get_emotion():
    """
    Analyzes the emotion of the text provided as a query parameter `textToAnalyze`.

    Returns:
        The result of the emotion detection, 
        which is a JSON-like response containing the detected emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] == "None":
        return(" Invalid text! Please try again!.", 400)
    return result

if __name__ == "__main__":
    app.run(debug=True)
