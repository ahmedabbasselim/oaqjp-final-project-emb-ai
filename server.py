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
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)
    # Extract the string emotion from the response
    anger = response ['anger']
    disgust = response ['disgust']
    fear = response ['fear']
    joy = response ['joy']
    sadness = response ['sadness']
    dominant_emotion = response ['dominant_emotion']
    if dominant_emotion == 'None':
        return  "Invalid text! Please try again!."
    # Return a formatted string with the emotion
    return f"For the given statement, the system response is 'anger':{anger}, 'disgust':{disgust}, 'fear':{fear}, 'joy':{joy} and 'sadness':{sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():  #Run render_template function on the HTML
    """Run render_template function on the HTML"""
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
