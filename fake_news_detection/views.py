from django.shortcuts import render
import joblib
from news_api import fetch_news

model = joblib.load('fake_news_model.pkl')

def classify_news(request):
    if request.method == 'POST':
        news_text = request.POST.get('news_text')
        prediction = model.predict([news_text])[0]
        external_data = fetch_news(news_text)
        return render(request, 'result.html', {'prediction': prediction, 'external_data': external_data})
    return render(request, 'classify.html')