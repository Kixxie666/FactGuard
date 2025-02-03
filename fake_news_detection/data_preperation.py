import os
import pandas as pd
from news_api import fetch_news

legit_path = 'E:\Factguard\Data\legit'
fake_path = 'E:\Factguard\Data\fake'

legit_files = os.listdir(legit_path)
fake_files = os.listdir(fake_path)

legit_data = [open(os.path.join(legit_path, file), 'r').read() for file in legit_files]
fake_data = [open(os.path.join(fake_path, file), 'r').read() for file in fake_files]

# Fetch additional news data
extra_news = fetch_news('politics')
extra_legit_data = [article['title'] for article in extra_news['articles']]

legit_df = pd.DataFrame({'text': legit_data + extra_legit_data, 'label': 'legit'})
fake_df = pd.DataFrame({'text': fake_data, 'label': 'fake'})

full_data = pd.concat([legit_df, fake_df])
full_data.to_csv('news_data.csv', index=False)