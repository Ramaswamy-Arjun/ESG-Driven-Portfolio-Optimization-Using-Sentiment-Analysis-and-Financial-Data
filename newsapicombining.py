import pandas as pd
from sklearn.utils import shuffle

data_file = r"C:\Users\arjun\OneDrive\Documents\ESG\upload.xlsx"  
df = pd.read_excel(data_file)

test_data_file = r"C:\Users\arjun\OneDrive\Documents\ESG\test_dataset.xlsx"  
test_df = pd.read_excel(test_data_file)

test_counts = test_df['label'].value_counts()
print(f"Current Test Data Distribution:\n{test_counts}")

max_class_count = test_counts.max()

needed_samples = {
    label: max_class_count - count
    for label, count in test_counts.items()
    if count < max_class_count
}

print(f"Samples needed to balance the test dataset: {needed_samples}")

neutral_needed = needed_samples.get('Neutral', 0)
positive_needed = needed_samples.get('Positive', 0)

neutral_samples = df[df['label'] == 'Neutral'].sample(n=neutral_needed, random_state=42)
positive_samples = df[df['label'] == 'Positive'].sample(n=positive_needed, random_state=42)

balanced_test_df = pd.concat([test_df, neutral_samples, positive_samples])
balanced_test_df = shuffle(balanced_test_df, random_state=42)

output_file = r"C:\Users\arjun\OneDrive\Documents\ESG\balanced_test_dataset.xlsx"
balanced_test_df.to_excel(output_file, index=False, engine="openpyxl")

print(f"\nTest dataset balanced and saved to: {output_file}")
print(f"Final Test Data Distribution:\n{balanced_test_df['label'].value_counts()}")
