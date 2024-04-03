import os
import requests  # Uncomment to import requests module
from dotenv import load_dotenv

load_dotenv()

# Define backend and sentiment analyzer URLs
BACKEND_URL = os.getenv('backend_url', default="http://localhost:3030")
SENTIMENT_ANALYZER_URL = os.getenv('sentiment_analyzer_url',
                                   default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = "&".join([f"{key}={value}" for key,
                       value in kwargs.items()]) if kwargs else ""
    request_url = f"{BACKEND_URL}{endpoint}?{params}"

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")


def analyze_review_sentiments(text):
    print("nigga")
    print(SENTIMENT_ANALYZER_URL)
    request_url = f"{SENTIMENT_ANALYZER_URL}analyze/{text}"
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = BACKEND_URL+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"An error occurred: {e}")
