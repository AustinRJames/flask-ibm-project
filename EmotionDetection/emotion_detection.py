import requests
import json

"""Detecting emotions"""
def emotion_detector(text_to_analyze):
    # define url for detector
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create payload object
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Set headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make post request with header and obj
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the response from the api
    emotion_data = json.loads(response.text)

    # Grab emotions
    emotions = emotion_data['emotionPredictions'][0]['emotion']

    # Find highest scored emotion
    dominant_emotion = max(emotions, key=emotions.get)

    emotions.update({'dominant_emotion': dominant_emotion})

    return emotions