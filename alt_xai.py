import pandas as pd
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from lime.lime_text import LimeTextExplainer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_path = r"C:\Users\arjun\OneDrive\Documents\ESG\content\finetuned_finbert"  
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model.to(device)
model.eval()

data_path = r"C:\Users\arjun\OneDrive\Documents\ESG\upload.xlsx"  
data = pd.read_excel(data_path)

if "Cleaned_Title" not in data.columns:
    raise ValueError("The dataset must contain a 'Cleaned_Title' column.")

texts = data["Cleaned_Title"].dropna().tolist()  


class LimeModelWrapper:
    def __init__(self, model, tokenizer, device):
        self.model = model
        self.tokenizer = tokenizer
        self.device = device

    def predict_proba(self, texts):
        """
        Predict probabilities for a list of texts using the fine-tuned FinBERT model.
        """
        if isinstance(texts, str):
            texts = [texts]

        encoded_inputs = self.tokenizer(
            texts,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors="pt"
        ).to(self.device)

        
        with torch.no_grad():
            outputs = self.model(**encoded_inputs)
            logits = outputs.logits
            probabilities = torch.nn.functional.softmax(logits, dim=-1).cpu().numpy()

        return probabilities


lime_model = LimeModelWrapper(model, tokenizer, device)

explainer = LimeTextExplainer(class_names=["Negative", "Neutral", "Positive"])

subset_texts = texts[:10]  


lime_explanations = []

print("Generating LIME explanations...")
for i, text in enumerate(subset_texts):
    print(f"Explaining text {i + 1}/{len(subset_texts)}: {text}")
    explanation = explainer.explain_instance(
        text_instance=text,
        classifier_fn=lime_model.predict_proba,
        num_features=10  
    )
    lime_explanations.append((text, explanation))


output_dir = "lime_explanations"
import os
os.makedirs(output_dir, exist_ok=True)

for i, (text, explanation) in enumerate(lime_explanations):

    explanation.save_to_file(f"{output_dir}/lime_explanation_{i + 1}.html")
    print(f"Explanation for text {i + 1} saved to {output_dir}/lime_explanation_{i + 1}.html")
