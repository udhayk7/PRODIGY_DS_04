import os
import zipfile
import urllib.request
import shutil

def download_nltk_data():
    """Download NLTK data manually without using nltk.download()"""
    # Create NLTK data directory in the project
    base_dir = os.path.dirname(os.path.dirname(__file__))
    nltk_data_dir = os.path.join(base_dir, 'nltk_data')
    os.makedirs(nltk_data_dir, exist_ok=True)

    # URLs for the required NLTK data
    urls = {
        'punkt': 'https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip',
        'stopwords': 'https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/stopwords.zip'
    }

    for data_name, url in urls.items():
        try:
            # Create directory for the specific data
            data_dir = os.path.join(nltk_data_dir, 'tokenizers' if data_name == 'punkt' else 'corpora')
            os.makedirs(data_dir, exist_ok=True)

            # Download zip file
            zip_path = os.path.join(nltk_data_dir, f'{data_name}.zip')
            print(f"Downloading {data_name}...")
            urllib.request.urlretrieve(url, zip_path)

            # Extract zip file
            print(f"Extracting {data_name}...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(data_dir)

            # Clean up zip file
            os.remove(zip_path)
            print(f"Successfully installed {data_name}")

        except Exception as e:
            print(f"Error downloading {data_name}: {str(e)}")

if __name__ == "__main__":
    download_nltk_data()
