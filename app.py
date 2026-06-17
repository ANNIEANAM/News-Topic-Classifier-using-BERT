import streamlit as st
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    pipeline
)

st.set_page_config(page_title="News Topic Classifier")

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(".")
    model = AutoModelForSequenceClassification.from_pretrained(".")

    classifier = pipeline(
        "text-classification",
        model=model,
        tokenizer=tokenizer
    )
    return classifier

classifier = load_model()

labels = {
    "LABEL_0": "World 🌍",
    "LABEL_1": "Sports ⚽",
    "LABEL_2": "Business 💼",
    "LABEL_3": "Sci/Tech 💻"
}

st.title("📰 News Topic Classifier using BERT")

headline = st.text_input(
    "Enter a news headline",
    placeholder="Apple launches new AI chip"
)

if st.button("Predict"):
    if headline.strip():
        result = classifier(headline)[0]

        category = labels.get(result["label"], result["label"])

        st.success(f"Category: {category}")
        st.info(f"Confidence: {result['score']:.2%}")
    else:
        st.warning("Please enter a headline.")
