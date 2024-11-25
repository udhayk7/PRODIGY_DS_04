"""
Configuration module for matplotlib and seaborn styling
"""
import matplotlib.pyplot as plt
import seaborn as sns

def setup_plotting_style():
    """Set up the plotting style for matplotlib and seaborn"""
    # Set seaborn style directly without using plt.style
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    sns.set_palette("husl")
    
    # Configure matplotlib for better visualization
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
    
    return plt, sns
