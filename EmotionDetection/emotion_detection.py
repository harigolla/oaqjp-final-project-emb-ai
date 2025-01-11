import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input, headers=header)
    json_data = json.loads(response.text)
    
    emotion_data = json_data['emotionPredictions'][0]['emotion']

    # Identify the dominant emotion
    dominant_emotion = max(emotion_data, key=emotion_data.get)

    # Construct the desired output format
    result = {
        'anger': emotion_data['anger'],
        'disgust': emotion_data['disgust'],
        'fear': emotion_data['fear'],
        'joy': emotion_data['joy'],
        'sadness': emotion_data['sadness'],
        'dominant_emotion': dominant_emotion
    }
    print(result)
    return result

if __name__ == '__main__':
    emotion_detector('I love this new technology')