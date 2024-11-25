import ssl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk
from wordcloud import WordCloud
import plotly.graph_objects as go

# Configure SSL for NLTK downloads
ssl._create_default_https_context = ssl._create_unverified_context

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except Exception as e:
    print(f"Warning: NLTK data download failed: {str(e)}")

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
