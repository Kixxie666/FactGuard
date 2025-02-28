import requests
from bs4 import BeautifulSoup
import joblib

# Load trained model
model = joblib.load("E:/Factguard/Data/fake_news_model.pkl")

def extract_text_from_url(url):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        return f"Error fetching the webpage: {e}"

    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')
    text_content = ' '.join([para.get_text() for para in paragraphs])

    if not text_content.strip():
        return "No readable content found on this webpage."

    return text_content

def classify_news_from_url(url):
    """
    Extracts text from the URL and classifies it using the trained model.
    """
    text_content = extract_text_from_url(url)

    if "Error" in text_content or "No readable content" in text_content:
        return text_content  

    prediction = model.predict([text_content])[0]

    if prediction == "fake":
        return "This webpage is likely FALSE"
    else:
        return "This webpage is likely LEGIT"
