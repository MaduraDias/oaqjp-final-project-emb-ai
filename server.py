"""
This module creates a Flask web application for detecting emotions in text.
It provides an endpoint `/emotionDetector` for analyzing the emotion of the given text.
"""

from flask import Flask,request,render_template
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

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    # Format the response
    emotion_items = [
        f"'{emotion}': {score}" for emotion, score in result.items() \
         if emotion != "dominant_emotion"
    ]

    if len(emotion_items) > 1:
        # Use ", " for all items except the last, and "and " for the last item
        emotion_scores = ", ".join(emotion_items[:-1]) + f", and {emotion_items[-1]}"
    else:
            # If there's only one item, no need for "and"
        emotion_scores = emotion_items[0]
    dominant_emotion = result["dominant_emotion"]
    response = [f"For the given statement, the system response is {emotion_scores}. \
                The dominant emotion is {dominant_emotion}."
    ]
    return response

@app.route('/')
def home():
    """
    Renders the home page (index.html) located in the templates folder.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
