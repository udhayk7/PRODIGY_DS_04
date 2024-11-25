"""
Configuration module for matplotlib and seaborn styling
"""
import matplotlib.pyplot as plt
import seaborn as sns

def setup_plotting_style():
    """Set up the plotting style for matplotlib and seaborn"""
    # Use the updated seaborn style name
    plt.style.use('seaborn-v0_8')
    
    # Set seaborn theme and palette
    sns.set_theme(style="whitegrid")
    sns.set_palette("husl")
    
    # Configure matplotlib for better visualization
    plt.rcParams['figure.figsize'] = [10, 6]
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['font.size'] = 12
    
    return plt, sns
