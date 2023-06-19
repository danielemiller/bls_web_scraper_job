import os
import shutil
from zipfile import ZipFile

def zip_and_move(url):
    # Replace slashes in the URL with underscores
    url_name = url.replace('/', '_')

    # Get the name of the most recent run folder
    folder_name = max([d for d in os.listdir("/home/astro/shared/projects/bls_scraping_data_job/downloads") if d.startswith(url_name)])

    # Create a new folder in the /data directory based on the URL
    os.makedirs(f"/home/astro/shared/projects/bls_scraping_data_job/data/{url_name}", exist_ok=True)

    # Create a ZipFile object
    with ZipFile(f"/home/astro/shared/projects/bls_scraping_data_job/data/{url_name}/{folder_name}.zip", 'w') as zipf:
        # Iterate over all the files in the folder
        for file in os.listdir(f"/home/astro/shared/projects/bls_scraping_data_job/downloads/{folder_name}"):
            # Add the file to the zip file
            zipf.write(os.path.join("/home/astro/shared/projects/bls_scraping_data_job/downloads", folder_name, file))

    # Move the zip file to the "data" directory
    shutil.move(f"/home/astro/shared/projects/bls_scraping_data_job/data/{url_name}/{folder_name}.zip", f"/home/astro/shared/projects/bls_scraping_data_job/data/{url_name}")

    # Return the name of the new folder
    return url_name
