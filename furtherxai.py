import os
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd
from tqdm import tqdm
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


lime_explanation_dir = r"C:\Users\arjun\OneDrive\Documents\ESG\lime_explanations" 


def parse_lime_explanations(directory):
    feature_counts = Counter()
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    logger.info(f"Found {len(files)} LIME explanation files to process.")

    for file_name in tqdm(files, desc="Parsing LIME explanations"):
        file_path = os.path.join(directory, file_name)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")
                
                feature_elements = soup.find_all("td", {"class": "lime-value"})
                for feature_element in feature_elements:
                    feature_text = feature_element.text.strip()
                    if feature_text:
                        feature_counts[feature_text] += 1
        except Exception as e:
            logger.error(f"Error parsing file {file_name}: {e}")

    return feature_counts


logger.info("Starting LIME explanation parsing and feature aggregation...")
feature_counts = parse_lime_explanations(lime_explanation_dir)


threshold = 5  
frequent_features = {feature: count for feature, count in feature_counts.items() if count >= threshold}


output_path = r"C:\Users\arjun\OneDrive\Documents\ESG\frequent_features.csv"
pd.DataFrame(list(frequent_features.items()), columns=["Feature", "Frequency"]).to_csv(output_path, index=False)
logger.info(f"Frequent features saved to: {output_path}")

logger.info("Suggestions for data augmentation or preprocessing:")
for feature, count in frequent_features.items():
    logger.info(f"Feature: {feature}, Frequency: {count}")
    logger.info(f"Suggestion: Consider adding more examples for '{feature}' or refining your tokenizer/preprocessing pipeline.")
