import os
import shutil
import logging
from zipfile import ZipFile

# Set up logging
logging.basicConfig(filename="/home/astro/shared/projects/bls_scraping_data_job/logs/zip_and_move.log", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")


def zip_and_move(url):
    try:
        # Replace slashes in the URL with underscores
        url_name = url.replace("/", "_")

        # Create a new directory in /home/astro/shared/projects/bls_scraping_data_job/data for this URL
        os.makedirs(f"/home/astro/shared/projects/bls_scraping_data_job/data/{url_name}", exist_ok=True)

        # Zip the contents of the download directory for this URL
        with ZipFile(f"/home/astro/shared/projects/bls_scraping_data_job/data/{url_name}/{url_name}.zip", "w") as zipf:
            for file in os.listdir(f"/home/astro/shared/projects/bls_scraping_data_job/downloads/{url_name}"):
                zipf.write(f"/home/astro/shared/projects/bls_scraping_data_job/downloads/{url_name}/{file}")

        # Move the zip file to the /data directory
        shutil.move(f"/home/astro/shared/projects/bls_scraping_data_job/downloads/{url_name}/{url_name}.zip", f"/home/astro/shared/projects/bls_scraping_data_job/data/{url_name}")

        # Delete the download directory for this URL
        shutil.rmtree(f"/home/astro/shared/projects/bls_scraping_data_job/downloads/{url_name}")

        logging.info(f"Successfully zipped and moved files for URL: {url}")

        return url_name

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
