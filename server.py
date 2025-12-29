"""
Module DocString
"""
import os

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


print("TEMPLATE FOLDER:", app.template_folder)
print("FILES:", os.listdir(app.template_folder))


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    emotionDetector route
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the sentiment_analyzer function and store the response
    emotion_data = emotion_detector(text_to_analyze)
    if emotion_data["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"
    emotion_data_list = []
    for key, value in emotion_data.items():
        if key == "dominant_emotion":
            continue
        emotion_data_list.append(f"'{key}': {value}")

    emotion_data_str = ", ".join(emotion_data_list)
    emotion_data_str += (
        f". The dominant emotion is <b>{emotion_data['dominant_emotion']}</b>"
    )
    return f"For the given statement, the system response is {emotion_data_str}"


@app.route("/")
def render_index_page():
    """
        Index page route
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# python3 server.py
