import ssl
import nltk
import certifi

# Configure SSL context to use certifi's certificates
ssl._create_default_https_context = ssl._create_unverified_context

def download_nltk_data():
    """Download required NLTK data with SSL verification disabled"""
    try:
        # Download required NLTK data
        nltk.download('punkt', quiet=False)
        nltk.download('stopwords', quiet=False)
        print("Successfully downloaded NLTK data!")
    except Exception as e:
        print(f"Error downloading NLTK data: {str(e)}")

if __name__ == "__main__":
    download_nltk_data()
