import pytest
import os
from selenium import webdriver


downloads_path = os.path.join(os.path.dirname(__file__), 'temp_downloads')


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": f"{downloads_path}"}
    options.add_experimental_option("prefs", prefs)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def clear_temp_downloads_folder():
    if os.path.exists(downloads_path):
        for file in os.listdir(downloads_path):
            file_path = os.path.join(downloads_path, file)
            os.remove(file_path)
