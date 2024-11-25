import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk
from wordcloud import WordCloud
import plotly.graph_objects as go

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Set up the plotting style
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)
sns.set_palette("husl")

# Configure matplotlib
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
    'grid.linestyle': '--',
    'grid.alpha': 0.6
})
