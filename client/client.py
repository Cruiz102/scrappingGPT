import requests

SERVER_URL = "http://your_ngrok_url"

def get_chat_data():
    try:
        response = requests.get(f"{SERVER_URL}/api/chat")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching chat data: {e}")
        return None