import requests
import json

def emotion_detector(text_to_analyze):
    
    # API endpoint and headers
    api_url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Payload to send to the API
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Make the POST request to the API
        response = requests.post(api_url, json=payload, headers=headers)

         # Check for 400 Bad Request
        if response.status_code == 400:
            error_res = {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion":None
                }
            return  error_res
            
         # Raise an exception if the status code indicates an error
        response.raise_for_status()

        emotions_dictionary = response.json()['emotionPredictions'][0]['emotion']
        
        #find dominant emotion and add to the dictionary
        dominant_emotion = max(emotions_dictionary, key=emotions_dictionary.get)
        emotions_dictionary['dominant_emotion'] = dominant_emotion

        return emotions_dictionary

    except requests.exceptions.RequestException as e:
        # Handle any errors during the request
        return f"An error occurred: {e}"