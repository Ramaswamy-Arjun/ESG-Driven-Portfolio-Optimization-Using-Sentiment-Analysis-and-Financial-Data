import pandas as pd
import os
from glob import glob

folder_path = r"C:\Users\arjun\OneDrive\Documents\ESG"

all_files = glob(os.path.join(folder_path, "*.csv"))

combined_df = pd.concat([pd.read_csv(file) for file in all_files], ignore_index=True)

unique_df = combined_df.drop_duplicates(subset=['title', 'content'], keep='first')

unique_df.to_csv(r"C:\Users\arjun\OneDrive\Documents\ESG\unique_combined_data.csv", index=False)

print(f"{len(unique_df)} unique records saved successfully!")
