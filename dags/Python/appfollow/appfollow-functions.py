import os
import time
import shutil
import datetime
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def navigate_the_scrape_link():
    logger = logging.getLogger(__class__.__name__)

        # Set the download directory
        download_dir = str(os.getpid()) + "_download_dir/"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        download_directory = download_dir

        chrome_options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values.automatic_downloads': 1,
                'download.default_directory': download_directory
        }

        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('window-size=1920x1080') #it solves to -headless problem
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('log-level=3') # hate the connection logs
        


        


