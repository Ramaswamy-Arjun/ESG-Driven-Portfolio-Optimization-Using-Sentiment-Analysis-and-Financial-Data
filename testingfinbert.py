import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
from sklearn.metrics import accuracy_score, classification_report

test_file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\test.xlsx" 
test_df = pd.read_excel(test_file_path)

label_mapping = {-1: 0, 0: 1, 1: 2}
test_df['mapped_labels'] = test_df['sentiment'].map(label_mapping)

test_df = test_df[test_df['Cleaned_Title'].notna()]  
test_df = test_df[test_df['Cleaned_Title'].str.strip() != '']  

model_path = r"C:\Users\arjun\OneDrive\Documents\ESG\content\finetuned_finbert" 
tokenizer = AutoTokenizer.from_pretrained(model_path)

test_encodings = tokenizer(
    list(test_df['Cleaned_Title']),
    truncation=True,
    padding=True,
    max_length=128
)

class ESGDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item

test_dataset = ESGDataset(test_encodings, list(test_df['mapped_labels']))

model = AutoModelForSequenceClassification.from_pretrained(model_path)

trainer = Trainer(model=model)

results = trainer.evaluate(test_dataset)

print("Evaluation Results:", results)

logits = trainer.predict(test_dataset).predictions
predictions = torch.argmax(torch.tensor(logits), dim=1).numpy()

true_labels = test_df['mapped_labels'].to_numpy()

accuracy = accuracy_score(true_labels, predictions)
print(f"Accuracy: {accuracy:.4f}")

report = classification_report(
    true_labels,
    predictions,
    target_names=["Negative", "Neutral", "Positive"]
)
print("Classification Report:\n", report)
