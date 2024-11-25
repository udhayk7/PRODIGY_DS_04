import os
import ssl
import nltk
import certifi
import urllib.request

def setup_ssl_context():
    cafile = certifi.where()
    context = ssl.create_default_context(cafile=cafile)
    return context

def download_nltk_data():
    """Download NLTK data using custom SSL context"""
    # Set up SSL context
    context = setup_ssl_context()
    
    try:
        # Set the SSL context for urllib
        urllib.request.urlopen = lambda url, **kwargs: urllib.request.urlopen(url, context=context, **kwargs)
        
        # Create NLTK data directory if it doesn't exist
        nltk_data_dir = os.path.expanduser('~/nltk_data')
        os.makedirs(nltk_data_dir, exist_ok=True)
        
        # Download required NLTK data
        nltk.download('punkt', download_dir=nltk_data_dir)
        nltk.download('stopwords', download_dir=nltk_data_dir)
        
        print("Successfully downloaded NLTK data!")
        
    except Exception as e:
        print(f"Error downloading NLTK data: {str(e)}")
        print("Trying alternative download method...")
        try:
            # Alternative method using direct SSL context
            ssl._create_default_https_context = ssl._create_unverified_context
            nltk.download('punkt')
            nltk.download('stopwords')
            print("Successfully downloaded NLTK data using alternative method!")
        except Exception as e2:
            print(f"Alternative download method also failed: {str(e2)}")

if __name__ == "__main__":
    download_nltk_data()
