import os
import pandas as pd
import pickle  
from news_api import fetch_news

<<<<<<< HEAD
LEGIT_PATH = r"E:/Factguard/Data/legit"  
FAKE_PATH = r"E:/Factguard/Data/fake"
SAVE_PATH_CSV = r"C:/Users/rgt20/Downloads/Dataguard/FactGuard/news_data.csv"
SAVE_PATH_PKL = r"C:/Users/rgt20/Downloads/Dataguard/FactGuard/news_data.pkl"
=======
# Load data properly
data_path = "E:/Factguard/Data/news_data.csv"

try:
    data = pd.read_csv(data_path)
except FileNotFoundError:
    print(f"Error: File {data_path} not found.")
    exit()

# Ensure 'text' and 'label' columns exist
if 'text' not in data.columns or 'label' not in data.columns:
    print("Error: The CSV file must contain 'text' and 'label' columns.")
    exit()
>>>>>>> 780b8b26 (Going back to wherer i was from a different version after the revert.)

if not os.path.exists(LEGIT_PATH) or not os.path.exists(FAKE_PATH):
    raise FileNotFoundError("Data folder missing. Check that E:/Factguard/Data exists!")

legit_files = os.listdir(LEGIT_PATH)
fake_files = os.listdir(FAKE_PATH)

<<<<<<< HEAD
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
=======
# Create a model pipeline (vectorisation + classification)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
>>>>>>> 780b8b26 (Going back to wherer i was from a different version after the revert.)

legit_data = [read_file(os.path.join(LEGIT_PATH, file)) for file in legit_files]
fake_data = [read_file(os.path.join(FAKE_PATH, file)) for file in fake_files]

<<<<<<< HEAD
extra_news = fetch_news('politics')
extra_legit_data = [article['title'] for article in extra_news['articles']]

legit_df = pd.DataFrame({'text': legit_data + extra_legit_data, 'label': 'legit'})
fake_df = pd.DataFrame({'text': fake_data, 'label': 'fake'})

full_data = pd.concat([legit_df, fake_df])

full_data.to_csv(SAVE_PATH_CSV, index=False, encoding='utf-8')
print(f" Data CSV saved to {SAVE_PATH_CSV}")

with open(SAVE_PATH_PKL, 'wb') as pkl_file:
    pickle.dump(full_data, pkl_file)
print(f" Data PKL saved to {SAVE_PATH_PKL}")
=======
# Save the trained model
joblib.dump(model, "E:/Factguard/Data/fake_news_model.pkl")

print("✅ Model trained and saved as fake_news_model.pkl!")
>>>>>>> 780b8b26 (Going back to wherer i was from a different version after the revert.)
