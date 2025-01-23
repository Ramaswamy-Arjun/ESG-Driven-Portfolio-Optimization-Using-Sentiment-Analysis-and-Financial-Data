import pandas as pd

file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\upload.xlsx"
esg_df = pd.read_excel(file_path)

print("Unique values in 'sentiment':", esg_df['sentiment'].unique())

non_integers = esg_df[~esg_df['sentiment'].apply(lambda x: isinstance(x, int))]
if not non_integers.empty:
    print("Non-integer values found in 'sentiment':")
    print(non_integers)
else:
    print("No non-integer values found in 'sentiment'.")

invalid_sentiments = esg_df[~esg_df['sentiment'].isin([-1, 0, 1])]
if not invalid_sentiments.empty:
    print("Invalid sentiment values found:")
    print(invalid_sentiments)
else:
    print("All values in 'sentiment' are valid.")
