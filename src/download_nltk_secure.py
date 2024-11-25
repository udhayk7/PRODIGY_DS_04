import os
import ssl
import nltk
import certifi
import urllib.request
from pathlib import Path

def get_project_nltk_data_dir():
    """Get the project-specific NLTK data directory"""
    current_dir = Path(__file__).parent
    project_root = current_dir.parent
    nltk_data_dir = project_root / 'nltk_data'
    return str(nltk_data_dir)

def configure_ssl():
    """Configure SSL context with proper certificate verification"""
    try:
        # Create and configure SSL context with certifi certificates
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        # Replace the default urlopen with our SSL-configured version
        original_urlopen = urllib.request.urlopen
        def urlopen_with_context(url, *args, **kwargs):
            return original_urlopen(url, *args, context=ssl_context, **kwargs)
        urllib.request.urlopen = urlopen_with_context
    except Exception as e:
        print(f"Warning: Could not configure SSL context with certifi: {e}")
        # Fallback to unverified context as last resort
        ssl._create_default_https_context = ssl._create_unverified_context

def download_nltk_data():
    """Download NLTK data with proper SSL handling"""
    # Set up the NLTK data directory
    nltk_data_dir = get_project_nltk_data_dir()
    os.makedirs(nltk_data_dir, exist_ok=True)
    
    # Add the custom data directory to NLTK's search path
    nltk.data.path.insert(0, nltk_data_dir)
    
    # Configure SSL before downloading
    configure_ssl()
    
    def download_package(package):
        try:
            print(f"Downloading {package} to {nltk_data_dir}...")
            nltk.download(package, download_dir=nltk_data_dir, raise_on_error=True)
            print(f"Successfully downloaded {package}")
            return True
        except Exception as e:
            print(f"Error downloading {package}: {str(e)}")
            return False

    # Required NLTK packages
    packages = ['punkt', 'stopwords']
    
    # Try downloading each package
    success = all(download_package(package) for package in packages)
    
    if success:
        print("\nAll NLTK data packages were downloaded successfully!")
        print(f"Data directory: {nltk_data_dir}")
    else:
        print("\nSome downloads failed. Please check the error messages above.")

if __name__ == "__main__":
    download_nltk_data()
