import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk
from wordcloud import WordCloud
import plotly.graph_objects as go

# Set up the plotting style
plt.style.use('seaborn-v0_8')  # Use the updated seaborn style name
sns.set_theme(style="whitegrid")  # Set seaborn theme
sns.set_palette("husl")  # Set color palette

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
