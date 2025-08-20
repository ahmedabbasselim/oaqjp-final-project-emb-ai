"""Web deployment of the application using Flask"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def emot_detector():
    """
    Retrieve the text to analyze from the request arguments, 
    then pass the text to the emotion_detector function
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion == 'None':
        return  "Invalid text! Please try again!."
    # Return a formatted string with the emotion
    return ("For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']} "
            f"and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")
@app.route("/")
def render_index_page():
    """Run render_template function on the HTML"""
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
