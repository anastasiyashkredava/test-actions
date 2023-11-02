import os
from time import sleep
from pages.base_page import BasePage
from pages.locators import download_page_locators as locators
from conftest import downloads_path


class DownLoadPage(BasePage):
    page_url = '/download'

    def download_sample_txt(self):
        self.find(locators.sample_txt).click()
        self.wait_until_download_completes()

    @staticmethod
    def wait_until_download_completes():
        dl_wait = True
        while dl_wait:
            sleep(1)
            for file_name in os.listdir(downloads_path):
                dl_wait = True if file_name.endswith('.crdownload') else False

    @staticmethod
    def check_sample_txt_content():
        sample_txt_path = os.path.join(downloads_path, 'sample.txt')
        with open(sample_txt_path, 'r') as file:
            return file.read().startswith('Lorem ipsum dolor sit amet')
