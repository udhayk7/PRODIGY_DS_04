import os
import ssl
import certifi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk
from wordcloud import WordCloud
import plotly.graph_objects as go
from pathlib import Path

def configure_nltk():
    """Configure NLTK with proper SSL and data directory setup"""
    # Set up project-specific NLTK data directory
    current_dir = Path(__file__).parent
    project_root = current_dir.parent
    nltk_data_dir = project_root / 'nltk_data'
    os.makedirs(nltk_data_dir, exist_ok=True)
    
    # Add our directory to NLTK's search path (at the beginning)
    nltk.data.path.insert(0, str(nltk_data_dir))
    
    try:
        # Configure SSL with certifi certificates
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        ssl._create_default_https_context = lambda: ssl_context
    except Exception as e:
        print(f"Warning: Using unverified SSL context due to: {e}")
        ssl._create_default_https_context = ssl._create_unverified_context
    
    # Download required NLTK data if not present
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', download_dir=str(nltk_data_dir))
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', download_dir=str(nltk_data_dir))

# Configure NLTK before anything else
configure_nltk()

# Set up the plotting style
plt.style.use('seaborn-v0_8-whitegrid')

# Additional seaborn configurations
sns.set_context("notebook", font_scale=1.2)
sns.set_palette("husl")

# Fine-tune the style
plt.rcParams.update({
    'figure.figsize': [10, 6],
    'figure.dpi': 100,
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16,
    'grid.alpha': 0.6
})
