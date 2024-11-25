import matplotlib.pyplot as plt

def print_available_styles():
    """Print all available matplotlib styles"""
    print("Available styles:")
    for style in plt.style.available:
        print(f"- {style}")

if __name__ == "__main__":
    print_available_styles()
