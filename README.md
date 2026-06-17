# News-Topic-Classifier-using-BERT
# News Topic Classifier Using BERT

## 1. Problem Statement & Objective

The objective of this project is to develop a News Topic Classifier using the BERT (Bidirectional Encoder Representations from Transformers) model. The model classifies news headlines into four categories: World, Sports, Business, and Sci/Tech. The project demonstrates the use of transfer learning and transformer-based architectures for text classification.

## 2. Dataset Loading & Preprocessing

The AG News Dataset was used for training and evaluation. The dataset contains news headlines and descriptions categorized into four classes.

Preprocessing steps included:

* Loading the dataset using Hugging Face Datasets.
* Tokenizing text using the BERT tokenizer.
* Padding and truncating sequences to a fixed length.
* Converting labels into numerical format.

Dataset Categories:

* World
* Sports
* Business
* Sci/Tech

## 3. Model Development & Training

The pre-trained bert-base-uncased model was fine-tuned for text classification.

Training Configuration:

* Model: bert-base-uncased
* Epochs: 1
* Batch Size: 8
* Optimizer: AdamW
* Framework: Hugging Face Transformers

The model was trained on a subset of the AG News dataset to reduce training time while maintaining strong performance.

## 4. Evaluation

The model was evaluated using Accuracy and F1-Score.

Results:

* Accuracy: 90.35%
* F1 Score: 90.34%

Classification metrics demonstrated that the model effectively categorized news headlines into their respective topics.

## 5. Deployment

The trained model was deployed using Streamlit, allowing users to enter news headlines and receive predicted topic categories in real time.

## 6. Final Summary & Insights

The BERT-based classifier achieved strong performance on the AG News dataset with over 90% accuracy. The project highlights the effectiveness of transfer learning for NLP tasks and demonstrates how transformer models can be deployed as interactive applications. The deployed application enables real-time topic classification of news headlines and provides a practical example of modern NLP model deployment.
