from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Init flask app
app = Flask("Emotion Detection:")

@app.route("/emotionDetector")
def emotion_detection():
    # Retrieve text to analyze
    text_to_analyze = request.args.get("textToAnalyze")

    # pass text to analyzer
    response = emotion_detector(text_to_analyze)

    # Extract values
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return "For the given statement, the system response is:\n 'anger': {}, 'disgust': {}, 'fear':{}, 'joy': {}, and 'sadness': {}. The most dominant emotion is {}.".format(anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
