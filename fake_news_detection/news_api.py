import requests

API_KEY = '8d8f7dcf72be487fbd759efcf3f44488'
BASE_URL = 'https://newsapi.org/v2/everything'

def fetch_news(query):
    params = {'q': query, 'apiKey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return None