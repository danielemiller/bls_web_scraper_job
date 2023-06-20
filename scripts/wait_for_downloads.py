import os
import subprocess
from scripts.zip_and_move import zip_and_move
from scripts.analyze_data import analyze_data
import time

def wait_for_downloads(download_dir):
    """
    Wait for downloads to finish by checking the download directory every second
    and waiting until no .part or .crdownload files are left.
    """
    while True:
        time.sleep(1)
        files = os.listdir(download_dir)
        if not any(f.endswith('.part') or f.endswith('.crdownload') for f in files):
            break

def main(url):
    # Run the bls_mega_web_scraper.py script
    subprocess.run(["python3", "./scripts/bls_mega_web_scraper.py", url])

    # Wait for all downloads to finish
    download_dir = f"/home/astro/shared/projects/bls_scraping_data_job/downloads/{url.replace('/', '_')}"
    wait_for_downloads(download_dir)

    # Get the name of the new folder created by zip_and_move.py
    new_folder_name = zip_and_move(url)

    # Analyze the data
    analyze_data(new_folder_name)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
