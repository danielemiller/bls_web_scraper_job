import os
import pandas as pd

# Get the name of the most recent data folder
folder_name = max([d for d in os.listdir("/home/astro/shared/projects/bls_web_scraper_gui/bls_scraping_data_job/data") if d.startswith("run_")])

# Create a DataFrame to store the data
data = pd.DataFrame()

# Iterate over all the files in the folder
for file in os.listdir(os.path.join("/home/astro/shared/projects/bls_web_scraper_gui/bls_scraping_data_job/data", folder_name)):
    # If the file is a CSV file
    if file.endswith(".csv"):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(os.path.join("/home/astro/shared/projects/bls_web_scraper_gui/bls_scraping_data_job/data", folder_name, file))
        # Append the DataFrame to the main DataFrame
        data = data.append(df, ignore_index=True)

# Save the DataFrame to a CSV file in the "analysis" directory
data.to_csv("/home/astro/shared/projects/bls_web_scraper_gui/bls_scraping_data_job/analysis/analysis_output.csv", index=False)
