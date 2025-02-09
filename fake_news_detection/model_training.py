import os
import pandas as pd
import pickle  # Save as PKL
from news_api import fetch_news

# Define correct file paths
LEGIT_PATH = r"E:/Factguard/Data/legit"  # Use raw string to avoid escape errors
FAKE_PATH = r"E:/Factguard/Data/fake"
SAVE_PATH_CSV = r"C:/Users/rgt20/Downloads/Dataguard/FactGuard/news_data.csv"
SAVE_PATH_PKL = r"C:/Users/rgt20/Downloads/Dataguard/FactGuard/news_data.pkl"

# Ensure data directories exist
if not os.path.exists(LEGIT_PATH) or not os.path.exists(FAKE_PATH):
    raise FileNotFoundError("❌ Data folder missing. Check that E:/Factguard/Data exists!")

# Load file names
legit_files = os.listdir(LEGIT_PATH)
fake_files = os.listdir(FAKE_PATH)

# Function to read files safely
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'rb') as f:  # Read as binary
            raw_data = f.read()
        try:
            return raw_data.decode('utf-8')  # Try UTF-8 first
        except UnicodeDecodeError:
            return raw_data.decode('latin-1')  # Fallback to Latin-1

# Read content from files
legit_data = [read_file(os.path.join(LEGIT_PATH, file)) for file in legit_files]
fake_data = [read_file(os.path.join(FAKE_PATH, file)) for file in fake_files]

# Fetch additional news data
extra_news = fetch_news('politics')
extra_legit_data = [article['title'] for article in extra_news['articles']]

# Create DataFrames
legit_df = pd.DataFrame({'text': legit_data + extra_legit_data, 'label': 'legit'})
fake_df = pd.DataFrame({'text': fake_data, 'label': 'fake'})

# Combine datasets
full_data = pd.concat([legit_df, fake_df])

# Save CSV file
full_data.to_csv(SAVE_PATH_CSV, index=False, encoding='utf-8')
print(f"✅ Data CSV saved to {SAVE_PATH_CSV}")

# Save as Pickle (`.pkl`) file
with open(SAVE_PATH_PKL, 'wb') as pkl_file:
    pickle.dump(full_data, pkl_file)
print(f"✅ Data PKL saved to {SAVE_PATH_PKL}")
