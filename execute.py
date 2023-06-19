import sys
from bls_mega_web_scraper import bls_mega_web_scraper
from zip_and_move import zip_and_move
from analyze_data import analyze_data

def execute(url):
    # Call the bls_mega_web_scraper script to download the zip files
    bls_mega_web_scraper(url)

    # Call the zip_and_move script to create a new folder and move the zip file into it
    folder_name = zip_and_move(url)

    # Call the analyze_data script to perform the analysis
    analyze_data(folder_name)

if __name__ == "__main__":
    url = sys.argv[1]
    execute(url)
