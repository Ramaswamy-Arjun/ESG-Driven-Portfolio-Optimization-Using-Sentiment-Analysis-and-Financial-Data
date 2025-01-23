import pandas as pd
import ast
import re
from sklearn.feature_extraction.text import TfidfVectorizer

file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\structured_esg_data.xlsx"   
esg_data = pd.read_excel(file_path)

print("Initial Data Preview:")
print(esg_data.head())
print("\nData Information:")
print(esg_data.info())

text_columns = ['Controversies', 'Ethical Flags']  
for col in text_columns:
    if col in esg_data.columns:
        esg_data[col] = esg_data[col].fillna("unknown") 

def clean_text(text):
    """Function to clean text by removing special characters and converting to lowercase."""
    if isinstance(text, str):
        text = re.sub(r'[^a-zA-Z\s]', '', text)  
        text = text.lower().strip() 
    return text

for col in text_columns:
    if col in esg_data.columns:
        esg_data[col] = esg_data[col].apply(clean_text)

if 'Controversies' in esg_data.columns:
    esg_data['Controversies List'] = esg_data['Controversies'].apply(
        lambda x: x.split(';') if isinstance(x, str) else []
    )


if 'Controversies' in esg_data.columns:
    tfidf_vectorizer = TfidfVectorizer(max_features=500, stop_words='english')  
    tfidf_matrix = tfidf_vectorizer.fit_transform(esg_data['Controversies'])
    tfidf_features = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
    esg_data = pd.concat([esg_data, tfidf_features], axis=1)

output_file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\preprocessed_esg_sentiment_data.csv"  
esg_data.to_csv(output_file_path, index=False)

print("\nPreprocessed Data Preview:")
print(esg_data.head())
