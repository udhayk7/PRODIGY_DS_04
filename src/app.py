import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# Set page config
st.set_page_config(
    page_title="Twitter Sentiment Analysis",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("🐦 Twitter Sentiment Analysis Dashboard")
st.markdown("Analyze sentiment patterns in Twitter data about various tech companies and products.")

# Load the data
@st.cache_data
def load_data():
    # Get the absolute path to the data file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, 'data', 'twitter_entity_sentiment.csv')
    
    try:
        df = pd.read_csv(data_path)
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.error(f"Attempted to load from: {data_path}")
        return None

df = load_data()

if df is not None:
    # Sidebar
    st.sidebar.header("Filters")
    selected_entities = st.sidebar.multiselect(
        "Select Entities",
        options=df['entity'].unique(),
        default=df['entity'].unique()
    )

    # Filter data based on selection
    filtered_df = df[df['entity'].isin(selected_entities)]

    # Main content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sentiment Distribution")
        sentiment_counts = filtered_df['sentiment'].value_counts()
        fig = px.pie(
            values=sentiment_counts.values,
            names=sentiment_counts.index,
            title="Overall Sentiment Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig)

    with col2:
        st.subheader("Entity-wise Sentiment")
        entity_sentiment = filtered_df.groupby(['entity', 'sentiment']).size().unstack(fill_value=0)
        fig = px.bar(
            entity_sentiment,
            title="Sentiment by Entity",
            barmode='group',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig)

    # Word clouds
    st.subheader("Word Clouds by Sentiment")
    col1, col2, col3 = st.columns(3)

    def generate_wordcloud(text, title, color='white'):
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color=color,
            colormap='viridis'
        ).generate(' '.join(text))
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title(title)
        return fig

    with col1:
        positive_text = filtered_df[filtered_df['sentiment'] == 'positive']['text']
        st.markdown("### Positive Sentiment")
        if not positive_text.empty:
            fig = generate_wordcloud(positive_text, "Positive Tweets")
            st.pyplot(fig)

    with col2:
        neutral_text = filtered_df[filtered_df['sentiment'] == 'neutral']['text']
        st.markdown("### Neutral Sentiment")
        if not neutral_text.empty:
            fig = generate_wordcloud(neutral_text, "Neutral Tweets")
            st.pyplot(fig)

    with col3:
        negative_text = filtered_df[filtered_df['sentiment'] == 'negative']['text']
        st.markdown("### Negative Sentiment")
        if not negative_text.empty:
            fig = generate_wordcloud(negative_text, "Negative Tweets")
            st.pyplot(fig)

    # Raw data
    st.subheader("Raw Data")
    st.dataframe(filtered_df)
