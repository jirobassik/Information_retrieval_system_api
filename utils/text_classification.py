import torch
from transformers import pipeline


def text_classification(text: str) -> dict:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # You can choose different models, like 'facebook/bart-large-mnli' or 'roberta-large-mnli'
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    class_descriptions = ["politics", "sports", "technology", "games", "medicine", "programming", "education",
                          "environment"]
    result = classifier(text, class_descriptions, device=device)
    for label, score in zip(result["labels"], result["scores"]):
        print(f"{label}: {score:.3f}")
    return [label for label, score in zip(result["labels"], result["scores"]) if score >= 0.1]
