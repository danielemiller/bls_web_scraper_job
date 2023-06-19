import logging
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Set up logging
logging.basicConfig(filename="oes_scraper.log", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

# Set up Firefox options
firefox_options = Options()

try:
    # Initialize the Firefox driver
    driver = webdriver.Firefox(options=firefox_options)

    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Go to the webpage
    driver.get(url)

    # Wait for the page to fully load
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

    # Find all the links on the page
    links = driver.find_elements(By.TAG_NAME, "a")

    # Iterate over the links
    for link in links:
        href = link.get_attribute("href")
        logging.info("Found link: " + href)
        # If the link href contains ".zip", click the link
        if ".zip" in href:
            link.click()
            # Add a wait time between clicks to avoid overwhelming the server
            time.sleep(2)

except Exception as e:
    logging.error("Exception occurred", exc_info=True)

finally:
    # Close the driver
    if "driver" in locals():
        driver.quit()
