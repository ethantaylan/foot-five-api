def send_message:
url = "https://api.wassenger.com/v1/messages"

payload = {
    "group": "33766704190-1624712064@g.uss",
    "message": "hello from API 2"
}
headers = {
    "Content-Type": "application/json",
    "Token": "5c3d36a4023c040b7fd8c47607c37df92877c0f8c7b3b7c00d90ee2d84b178061faf65bf3627c3f9"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())