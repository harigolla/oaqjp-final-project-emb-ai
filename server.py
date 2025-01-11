"""
Flask web application for detecting emotions from text input.

This module provides a web interface where users can submit text for
emotion analysis, and it returns the detected emotions along with
the dominant emotion.

Routes:
    - `/`: Renders the index page with a text input form.
    - `/emotionDetector`: Processes text input and returns emotion analysis.

Usage:
    Run the script and visit `http://localhost:5000` in a web browser.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the homepage with a text input form for emotion analysis.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotions in the provided text and returns the result.

    Returns:
        str: Analysis result or error message if no dominant emotion is detected.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if not dominant_emotion:
        return "Invalid text! Please try again!"

    del response['dominant_emotion']
    return f"For the given statement, the system response is {response}.\
            The dominant emotion is {dominant_emotion}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
