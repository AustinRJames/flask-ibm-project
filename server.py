"""SERVER Class for Emotion detection"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Init flask app
app = Flask("Emotion Detection:")

@app.route("/emotionDetector")
def emotion_detection():
    """
    Emotion detector function.
    
    Analyzes text input for emotional content and returns emotion scores
    along with the dominant emotion.
    
    Returns:
        str: Formatted string with emotion analysis results or error message
    """
    # Retrieve text to analyze
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or text_to_analyze.strip() == "":
        # Return None values for blank input
        return "Invalid text! Try again!"

    # pass text to analyzer
    response = emotion_detector(text_to_analyze)

    if response.status_code == 400:
        return "Invalid text! Please try again!"

    if response.status_code == 500:
        return "No response given"

    # Extract values
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (f"For the given statement, the system response is:\n"
            f"'anger': {anger_score}, 'disgust': {disgust_score}, "
            f"'fear': {fear_score}, 'joy': {joy_score}, and "
            f"'sadness': {sadness_score}. The most dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """
    Default route that renders the main index page.
    
    Returns:
        str: Rendered HTML template for the index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
