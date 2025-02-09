import os
import pandas as pd
import pickle  # To save the PKL file
from news_api import fetch_news

# External paths
LEGIT_PATH = r"E:\Factguard\Data\legit"
FAKE_PATH = r"E:\Factguard\Data\fake"
SAVE_PATH = r"C:\Users\rgt20\Downloads\Dataguard\FactGuard\news_data.pkl"

legit_files = os.listdir(LEGIT_PATH)
fake_files = os.listdir(FAKE_PATH)

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'rb') as f: 
            raw_data = f.read()
        try:
            return raw_data.decode('utf-8')  
        except UnicodeDecodeError:
            return raw_data.decode('latin-1')  

legit_data = [read_file(os.path.join(LEGIT_PATH, file)) for file in legit_files]
fake_data = [read_file(os.path.join(FAKE_PATH, file)) for file in fake_files]

extra_news = fetch_news('politics')
extra_legit_data = [article['title'] for article in extra_news['articles']]

legit_df = pd.DataFrame({'text': legit_data + extra_legit_data, 'label': 'legit'})
fake_df = pd.DataFrame({'text': fake_data, 'label': 'fake'})

full_data = pd.concat([legit_df, fake_df])

csv_path = os.path.join(LEGIT_PATH, "..", "news_data.csv") 
full_data.to_csv(csv_path, index=False)

with open(SAVE_PATH, 'wb') as pkl_file:
    pickle.dump(full_data, pkl_file)

print(f"Data saved successfully to {SAVE_PATH}")
