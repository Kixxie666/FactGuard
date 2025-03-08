from django.shortcuts import render
import joblib
import os
from .news_api import fetch_news

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "fake_news_model.pkl")


model = joblib.load(MODEL_PATH)

def classify_news(request):
    prediction_label = None 

    if request.method == 'POST':
        news_url = request.POST.get('news_url')

        if news_url:
            prediction = model.predict([news_url])[0]  
            prediction_label = "Legitimate" if prediction == 1 else "Fake"
        else:
            prediction_label = "No URL provided"

        return render(request, 'fake_news_detection/result.html', {
            'prediction': prediction_label,
            'news_url': news_url 
        })
    
    return render(request, 'fake_news_detection/classify.html')
