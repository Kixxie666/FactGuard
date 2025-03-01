import os
import pandas as pd
import pickle
import joblib
from news_api import fetch_news
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


LEGIT_PATH = r"E:/Factguard/Data/legit"
FAKE_PATH = r"E:/Factguard/Data/fake"
SAVE_PATH_CSV = r"C:/Users/rgt20/Downloads/Dataguard/FactGuard/news_data.csv"
SAVE_PATH_PKL = r"C:/Users/rgt20/Downloads/Dataguard/FactGuard/news_data.pkl"
MODEL_PATH = r"E:/Factguard/Data/fake_news_model.pkl"


if not os.path.exists(LEGIT_PATH) or not os.path.exists(FAKE_PATH):
    raise FileNotFoundError("Data folder missing. Check that E:/Factguard/Data exists!")


legit_files = os.listdir(LEGIT_PATH)
fake_files = os.listdir(FAKE_PATH)

def read_file(file_path):
    """Read file content with encoding fallback."""
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


full_data.to_csv(SAVE_PATH_CSV, index=False, encoding='utf-8')
print(f"✅ Data CSV saved to {SAVE_PATH_CSV}")

with open(SAVE_PATH_PKL, 'wb') as pkl_file:
    pickle.dump(full_data, pkl_file)
print(f"✅ Data PKL saved to {SAVE_PATH_PKL}")


model = make_pipeline(TfidfVectorizer(), MultinomialNB())
X, y = full_data['text'], full_data['label']
model.fit(X, y)


joblib.dump(model, MODEL_PATH)
print(f"✅ Model trained and saved as {MODEL_PATH}!")
