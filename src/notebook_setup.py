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

# Set up the plotting style correctly
plt.style.use('seaborn-v0_8')  # Use the updated seaborn style name
sns.set_theme(style="whitegrid")  # Set seaborn theme
sns.set_palette("husl")  # Set color palette

# Configure matplotlib for better visualization
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 12
