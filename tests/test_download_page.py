from pages.download_page import DownLoadPage

@pytest.mark.skip('bug')
def test_sample_txt_content(driver, clear_temp_downloads_folder):
    download_page = DownLoadPage(driver)
    download_page.open()
    download_page.download_sample_txt()
    assert download_page.check_sample_txt_content()
