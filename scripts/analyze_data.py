import os
import pandas as pd
from zipfile import ZipFile
import shutil

def analyze_data(folder_name):
    # Create a new folder in the /analysis directory
    os.makedirs(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}", exist_ok=True)

    # Unzip the main zip file into this new folder
    with ZipFile(f"/home/astro/shared/projects/bls_scraping_data_job/data/{folder_name}/{folder_name}.zip", 'r') as zipf:
        zipf.extractall(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}")

    # Iterate over each file in the main zip file
    for file in os.listdir(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}"):
        if file.endswith(".zip"):
            # Create a new directory named after the zip file
            zip_file_name = os.path.splitext(file)[0]
            os.makedirs(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{zip_file_name}/data", exist_ok=True)
            os.makedirs(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{zip_file_name}/reports", exist_ok=True)

            # Move the zip file into the /data directory and unzip it there
            shutil.move(file, f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{zip_file_name}/data/{file}")
            with ZipFile(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{zip_file_name}/data/{file}", 'r') as zipf:
                zipf.extractall(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{zip_file_name}/data")

            # Read each Excel file into a pandas DataFrame and perform the preliminary analysis
            for excel_file in os.listdir(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{zip_file_name}/data"):
                if excel_file.endswith(".xls") or excel_file.endswith(".xlsx"):
                    df = pd.read_excel(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{zip_file_name}/data/{excel_file}")

                    # Perform the preliminary analysis (replace this with your actual analysis)
                    analysis_results = df.describe()

                    # Save the analysis results as a .txt file in the /reports directory
                    with open(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{zip_file_name}/reports/{excel_file}_analysis.txt", 'w') as f:
                        f.write(str(analysis_results))
        elif file.endswith(".xls") or file.endswith(".xlsx"):
            # Read the Excel file into a pandas DataFrame and perform the preliminary analysis
            df = pd.read_excel(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{file}")

            # Perform the preliminary analysis (replace this with your actual analysis)
            analysis_results = df.describe()

            # Save the analysis results as a .txt file in the /reports directory
            with open(f"/home/astro/shared/projects/bls_scraping_data_job/analysis/{folder_name}/{file}_analysis.txt", 'w') as f:
                f.write(str(analysis_results))
