import os
import shutil
from zipfile import ZipFile

def zip_and_move(url):
    # Get the name of the most recent run folder
    folder_name = max([d for d in os.listdir("/home/astro/Downloads") if d.startswith("run_")])

    # Create a new folder in the /data directory based on the URL
    new_folder_name = url.replace('/', '_')
    os.makedirs(f"/home/astro/shared/projects/bls_scraping_data_job/data/{new_folder_name}", exist_ok=True)

    # Create a ZipFile object
    with ZipFile(f"/home/astro/shared/projects/bls_scraping_data_job/data/{new_folder_name}/{folder_name}.zip", 'w') as zipf:
        # Iterate over all the files in the folder
        for file in os.listdir(folder_name):
            # Add the file to the zip file
            zipf.write(os.path.join(folder_name, file))

    # Return the name of the new folder
    return new_folder_name
