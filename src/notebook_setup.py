import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk
from wordcloud import WordCloud
import plotly.graph_objects as go

# Set NLTK data path to a local directory in the project
nltk_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'nltk_data')
os.makedirs(nltk_data_path, exist_ok=True)
nltk.data.path.append(nltk_data_path)

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
