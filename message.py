import requests
import os 

def send_message(message):
    payload = {
        "group": "120363312585357097@g.us",
        "message": message
    }
    headers = {
        "Content-Type": "application/json",
        "Token": os.environ.get("WASSENGER_TOKEN")
    }

    response = requests.post('https://api.wassenger.com/v1/messages', json=payload, headers=headers)
    print(response.json())