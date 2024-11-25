import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    """Download the Twitter Entity Sentiment Analysis dataset from Kaggle"""
    
    # Create data directory if it doesn't exist
    os.makedirs('../data', exist_ok=True)
    
    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()
    
    # Download dataset
    dataset_name = "jp797498e/twitter-entity-sentiment-analysis"
    api.dataset_download_files(dataset_name, path='../data', unzip=True)
    
    print("Dataset downloaded successfully to the data directory!")

if __name__ == "__main__":
    download_dataset()
