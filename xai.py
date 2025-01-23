import shap
import pandas as pd
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from tqdm import tqdm
import json

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

def predict_proba(texts):
    """
    Predict probabilities for a list of texts using the fine-tuned FinBERT model.
    """
    
    print(f"Debug: Input to predict_proba - Type: {type(texts)}, Content: {texts[:5] if isinstance(texts, list) else texts}")
    
    if isinstance(texts, str):
        texts = [texts]
    elif isinstance(texts, list):
        if isinstance(texts[0], list):  
            texts = [item for sublist in texts for item in sublist]
        texts = [str(t) for t in texts if isinstance(t, str)]  
    else:
        raise ValueError("Input to predict_proba must be a string or a list of strings.")

    encoded_inputs = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors="pt"
    ).to(device)

    with torch.no_grad():
        outputs = model(**encoded_inputs)
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1).cpu().numpy()

    return probabilities

subset_texts = texts[:100]  
masker = shap.maskers.Text(tokenizer)

print("Initializing SHAP Explainer...")
explainer = shap.Explainer(predict_proba, masker)
print("SHAP Explainer initialized.")

print("Computing SHAP values...")
try:
    shap_values = explainer(subset_texts)
except Exception as e:
    print(f"Error while computing SHAP values: {e}")
    raise

print("Analyzing SHAP values...")

for i, explanation in enumerate(shap_values[:5]):  
    print(f"\nText {i + 1}: {subset_texts[i]}")
    print(f"SHAP values for each feature/token:")
    for token, value in zip(explanation.data, explanation.values):
        print(f"  {token}: {value}")

print("\nExporting SHAP values to a JSON file...")
shap_export = []
for explanation in shap_values:
    shap_export.append({
        "tokens": explanation.data,
        "values": explanation.values.tolist()
    })

output_file = "shap_values.json"
with open(output_file, "w") as f:
    json.dump(shap_export, f)
print(f"SHAP values exported to {output_file}")
