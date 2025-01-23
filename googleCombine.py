import pandas as pd

file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\preprocessed_ESG.xlsx"
esg_df = pd.read_excel(file_path)

esg_df = esg_df.dropna(subset=['sentiment'])

esg_df['sentiment'] = esg_df['sentiment'].astype(int)

cleaned_file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\upload.xlsx"
esg_df.to_excel(cleaned_file_path, index=False)

print(f"Cleaned dataset saved to {cleaned_file_path}")
