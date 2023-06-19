import os
import shutil
from zipfile import ZipFile

# Get the name of the most recent run folder
folder_name = max([d for d in os.listdir("/home/astro/Downloads") if d.startswith("run_")])

# Create a ZipFile object
with ZipFile(folder_name + ".zip", w) as zipf:
    # Iterate over all the files in the folder
    for file in os.listdir(os.path.join("/home/astro/Downloads", folder_name)):
        # Add the file to the zip file
        zipf.write(os.path.join("/home/astro/Downloads", folder_name, file))

# Move the zip file to the "data" directory
shutil.move(os.path.join("/home/astro/Downloads", folder_name + ".zip"), "/home/astro/shared/projects/bls_web_scraper_gui/bls_scraping_data_job/data")

# Delete the original run folder
shutil.rmtree(os.path.join("/home/astro/Downloads", folder_name))
