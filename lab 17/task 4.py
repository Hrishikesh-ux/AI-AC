import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download necessary NLTK components if you haven't already
# nltk.download(['punkt', 'wordnet', 'stopwords'])

# --- 1. Generate Sample Data ---
data = {
    'tweet_id': [1, 2, 3, 4, 5],
    'text': [
        "I love this new product! So happy! Check it out: http://example.com/happy 😊 #awesome",
        "Disappointed with the service, never again! 😡👎",
        "The quick brown fox jumps over the lazy dog.",
        "Sales are up 15% this quarter!!! YAYYYY!",
        "Is this the official hr or Human Resources page? Plz reply."
    ],
    'sentiment': ['Positive', 'Negative', 'Neutral', 'Positive', 'Neutral']
}
df_social = pd.DataFrame(data)

# --- 2. Text Preprocessing Function ---
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove special characters (keep letters and spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords and apply lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word.isalpha()]
    # Join tokens back into a string
    return " ".join(tokens)

# --- 3. Apply Preprocessing ---
df_social['cleaned_text'] = df_social['text'].apply(preprocess_text)

# --- 4. Display Output and Assertions ---
print("--- Task 4: Social Media Dataset Preparation ---")
print("\nOriginal Data:")
print(df_social[['text', 'sentiment']].head())
print("\nProcessed Data:")
print(df_social[['cleaned_text', 'sentiment']])

# Assert Test Cases
assert df_social['cleaned_text'].iloc[0] == 'love new product happy awesome'
assert 'disappointed service never' in df_social['cleaned_text'].iloc[1]
assert df_social['cleaned_text'].iloc[4] == 'official hr human resource plz reply'