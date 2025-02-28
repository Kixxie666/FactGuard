from django.shortcuts import render
import joblib
import os
from .news_api import fetch_news

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "fake_news_model.pkl")


model = joblib.load(MODEL_PATH)

def classify_news(request):
    if request.method == 'POST':
        news_text = request.POST.get('news_text')
        prediction = model.predict([news_text])[0]
        return render(request, 'fake_news_detection/result.html', {'prediction': prediction})
    return render(request, 'fake_news_detection/classify.html')
