# Twitter Sentiment Analysis Dashboard

## Project Overview
This project is a Twitter sentiment analysis dashboard that visualizes sentiment patterns in social media data. It provides insights into public opinion about various tech companies and their products.

## Features
- Interactive sentiment distribution visualization
- Entity-wise sentiment analysis
- Word clouds for positive, neutral, and negative sentiments
- Filterable raw data view
- Real-time data updates

## Project Structure
```
PRODIGY_DS_04/
├── data/
│   └── twitter_entity_sentiment.csv
├── src/
│   ├── app.py              # Main Streamlit dashboard
│   ├── notebook_setup.py   # Jupyter notebook setup
│   └── test_app.py         # Test application
├── notebooks/
│   └── sentiment_analysis.ipynb
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run src/app.py
   ```

## Technologies Used
- Python 3.12
- Streamlit for web interface
- Pandas for data manipulation
- Plotly for interactive visualizations
- TextBlob for sentiment analysis
- NLTK for text processing
- WordCloud for word cloud generation

## Data
The project uses Twitter data with the following structure:
- tweet_id: Unique identifier for each tweet
- text: Tweet content
- entity: Company/product mentioned
- sentiment: Sentiment classification (positive/neutral/negative)

## Features
1. Sentiment Distribution
   - Pie chart showing overall sentiment distribution
   - Interactive filtering capabilities

2. Entity Analysis
   - Bar chart showing sentiment by entity
   - Entity-wise comparison

3. Word Clouds
   - Visual representation of common words
   - Separate clouds for each sentiment

4. Raw Data View
   - Searchable and sortable data table
   - Full tweet content access
