import pandas as pd
from news_api import fetch_news  # Ensure this module is available

# Define CSV file paths (these should be FILES, not directories)
legit_path = "E:/Factguard/Data/legit/True.csv"
fake_path = "E:/Factguard/Data/fake/Fake.csv"

# Read CSV files properly
try:
    legit_df = pd.read_csv(legit_path)
    fake_df = pd.read_csv(fake_path)
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

if 'text' not in legit_df.columns or 'text' not in fake_df.columns:
    print("Error: CSV files must contain a 'text' column.")
    exit()

legit_df['label'] = 'legit'
fake_df['label'] = 'fake'


extra_legit_data = []
extra_news = fetch_news('politics')

if extra_news and 'articles' in extra_news:
    extra_legit_data = [article['title'] for article in extra_news['articles'] if 'title' in article]


extra_legit_df = pd.DataFrame({'text': extra_legit_data, 'label': 'legit'})


full_data = pd.concat([legit_df, fake_df, extra_legit_df], ignore_index=True)


full_data.to_csv("E:/Factguard/Data/news_data.csv", index=False)

print("Dataset successfully created and saved as news_data.csv!")

data = pd.read_csv("E:/Factguard/Data/news_data.csv")
print(data.head())
print(data['label'].value_counts())

