import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Set default style for better visualizations
plt.style.use('default')
sns.set_theme(style="whitegrid")

def load_data(file_path):
    """Load and display basic information about the dataset"""
    df = pd.read_csv(file_path)
    print("Dataset Info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    return df

def clean_text(text):
    """Clean and preprocess text data"""
    # Convert to lowercase
    text = str(text).lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove user mentions
    text = re.sub(r'@\w+', '', text)
    
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    return text.strip()

def get_sentiment(text):
    """Calculate sentiment score using TextBlob"""
    return TextBlob(text).sentiment.polarity

def analyze_sentiments(df):
    """Perform sentiment analysis on the dataset"""
    # Clean text
    df['cleaned_text'] = df['text'].apply(clean_text)
    
    # Calculate sentiment scores
    df['sentiment_score'] = df['cleaned_text'].apply(get_sentiment)
    
    # Categorize sentiment
    df['sentiment_category'] = pd.cut(df['sentiment_score'],
                                    bins=[-1, -0.1, 0.1, 1],
                                    labels=['Negative', 'Neutral', 'Positive'])
    return df

def plot_sentiment_distribution(df):
    """Plot sentiment distribution"""
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='sentiment_score', bins=50)
    plt.title('Distribution of Sentiment Scores')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Count')
    plt.show()

def plot_entity_sentiment(df):
    """Plot average sentiment by entity"""
    entity_sentiment = df.groupby('entity')['sentiment_score'].mean().sort_values()
    plt.figure(figsize=(12, 6))
    entity_sentiment.plot(kind='bar')
    plt.title('Average Sentiment Score by Entity')
    plt.xlabel('Entity')
    plt.ylabel('Average Sentiment Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def generate_wordclouds(df):
    """Generate word clouds for positive and negative sentiments"""
    # Positive sentiment word cloud
    positive_text = ' '.join(df[df['sentiment_score'] > 0]['cleaned_text'])
    wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_positive, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud - Positive Sentiment')
    plt.show()
    
    # Negative sentiment word cloud
    negative_text = ' '.join(df[df['sentiment_score'] < 0]['cleaned_text'])
    wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(negative_text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_negative, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud - Negative Sentiment')
    plt.show()

def create_interactive_plots(df):
    """Create interactive plots using plotly"""
    # Sentiment distribution
    fig = px.histogram(df, x='sentiment_score', nbins=50,
                      title='Distribution of Sentiment Scores',
                      labels={'sentiment_score': 'Sentiment Score', 'count': 'Frequency'})
    fig.show()
    
    # Entity sentiment analysis
    entity_sentiment_df = df.groupby('entity').agg({
        'sentiment_score': ['mean', 'count']
    }).reset_index()
    
    fig = px.scatter(entity_sentiment_df,
                    x=('sentiment_score', 'mean'),
                    y=('sentiment_score', 'count'),
                    text='entity',
                    title='Entity Sentiment Analysis',
                    labels={'sentiment_score': 'Average Sentiment Score',
                           'count': 'Number of Mentions'})
    fig.show()

def main():
    # Load the dataset
    df = load_data('../data/twitter_entity_sentiment.csv')
    
    # Perform sentiment analysis
    df = analyze_sentiments(df)
    
    # Create visualizations
    plot_sentiment_distribution(df)
    plot_entity_sentiment(df)
    generate_wordclouds(df)
    create_interactive_plots(df)

if __name__ == "__main__":
    main()
