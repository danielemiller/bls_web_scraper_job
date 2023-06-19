import subprocess
import sys
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename="execute.log", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

# Get the list of URLs from the command-line arguments
urls = sys.argv[1:]

# Define the paths to the scripts
web_scraper_script = "/home/astro/shared/projects/bls_web_scraper_gui/bls_scraping_data_job/scripts/bls_mega_web_scraper.py"
zip_and_move_script = "/home/astro/shared/projects/bls_web_scraper_gui/bls_scraping_data_job/scripts/zip_and_move.py"
data_analysis_script = "/home/astro/shared/projects/bls_web_scraper_gui/bls_scraping_data_job/scripts/analyze_data.py"

# Iterate over the URLs
for url in urls:
    try:
        # Run the web scraper script
        subprocess.check_call(["python3", web_scraper_script, url])
        # Run the zip and move script
        subprocess.check_call(["python3", zip_and_move_script])
        # Run the data analysis script
        subprocess.check_call(["python3", data_analysis_script])
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while processing the URL {url}. Moving on to the next URL.", exc_info=True)
        print(f"An error occurred while processing the URL {url}. Moving on to the next URL.")
