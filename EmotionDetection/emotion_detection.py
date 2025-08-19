import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the EMOTION detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # header to specify the model ID for the emotion detection service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200: 
        # Extracting emotion dictionary from the formatted response
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        # Extracting dominant emotion from emotion dictionary
        dominant_emotion_key = max(emotion, key = emotion.get)
        #Adding new dominant_emotion_key to emotion dictionary
        emotion['dominant_emotion'] = dominant_emotion_key
        return emotion
    elif response.status_code == 400:
        emotion = {'anger': 'None', 'disgust': 'None', 'fear': 'None', 'joy': 'None', 'sadness': 'None', 'dominant_emotion': 'None'}
        return emotion
    