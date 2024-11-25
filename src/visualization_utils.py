"""
Utility functions for data visualization
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_entity_sentiment_scatter(df: pd.DataFrame) -> go.Figure:
    """
    Create an interactive scatter plot of entity sentiment analysis
    
    Args:
        df: DataFrame with columns 'entity' and 'sentiment_score'
        
    Returns:
        Plotly figure object
    """
    # Group by entity and calculate mean sentiment and count
    entity_sentiment = df.groupby('entity').agg({
        'sentiment_score': ['mean', 'count']
    }).reset_index()
    
    # Flatten column names
    entity_sentiment.columns = ['entity', 'avg_sentiment', 'mention_count']
    
    # Create scatter plot
    fig = px.scatter(
        entity_sentiment,
        x='avg_sentiment',
        y='mention_count',
        text='entity',
        title='Entity Sentiment Analysis',
        labels={
            'avg_sentiment': 'Average Sentiment Score',
            'mention_count': 'Number of Mentions'
        }
    )
    
    # Update layout
    fig.update_traces(
        textposition='top center',
        marker=dict(size=10),
        mode='markers+text'
    )
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        title_x=0.5,
        title_font_size=20
    )
    
    return fig

def create_sentiment_distribution(df: pd.DataFrame) -> go.Figure:
    """
    Create a pie chart showing sentiment distribution
    
    Args:
        df: DataFrame with 'sentiment' column
        
    Returns:
        Plotly figure object
    """
    sentiment_counts = df['sentiment'].value_counts()
    
    fig = px.pie(
        values=sentiment_counts.values,
        names=sentiment_counts.index,
        title='Sentiment Distribution',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20
    )
    
    return fig

def create_entity_sentiment_bars(df: pd.DataFrame) -> go.Figure:
    """
    Create a bar chart showing sentiment by entity
    
    Args:
        df: DataFrame with 'entity' and 'sentiment_score' columns
        
    Returns:
        Plotly figure object
    """
    entity_sentiment = df.groupby('entity')['sentiment_score'].mean().sort_values()
    
    fig = px.bar(
        x=entity_sentiment.values,
        y=entity_sentiment.index,
        orientation='h',
        title='Average Sentiment by Entity',
        labels={
            'x': 'Average Sentiment Score',
            'y': 'Entity'
        }
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        showlegend=False,
        plot_bgcolor='white'
    )
    
    return fig
