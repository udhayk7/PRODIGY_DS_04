# Social Media Sentiment Analysis

## Project Overview
This project analyzes sentiment patterns in social media data to understand public opinion and attitudes towards specific topics or brands. Using Twitter entity sentiment analysis dataset, we perform various analyses to extract meaningful insights about public perception.

## Features
- Sentiment analysis of tweets
- Topic/entity detection
- Sentiment visualization
- Trend analysis over time
- Brand sentiment comparison

## Dataset
The project uses the Twitter Entity Sentiment Analysis dataset from Kaggle, which contains:
- Tweet content
- Entity mentions
- Sentiment labels
- Temporal information

## Project Structure
```
├── data/               # Dataset files
├── notebooks/         # Jupyter notebooks
├── src/              # Source code
└── requirements.txt  # Project dependencies
```

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Download the dataset from Kaggle and place it in the `data` directory
4. Run the Jupyter notebooks in the `notebooks` directory

## Analysis Components
1. Data Preprocessing
   - Text cleaning
   - Entity extraction
   - Sentiment scoring

2. Exploratory Data Analysis
   - Sentiment distribution
   - Entity frequency analysis
   - Temporal patterns

3. Visualization
   - Sentiment trends
   - Word clouds
   - Entity-sentiment relationships
   - Interactive dashboards

## Technologies Used
- Python
- Pandas
- NLTK
- TextBlob
- Scikit-learn
- Matplotlib/Seaborn
- Plotly
