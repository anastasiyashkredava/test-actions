from pages.base_page import BasePage
from pages.locators import floating_menu_page_locators as locators


class FloatingMenuPage(BasePage):
    page_url = '/floating_menu'

    home_url = 'https://the-internet.herokuapp.com/floating_menu#home'
    news_url = 'https://the-internet.herokuapp.com/floating_menu#news'
    about_url = 'https://the-internet.herokuapp.com/floating_menu#about'
    contact_url = 'https://the-internet.herokuapp.com/floating_menu#contact'

    def click_home(self):
        self.find(locators.home_menu).click()

    def click_news(self):
        self.find(locators.news_menu).click()

    def click_contact(self):
        self.find(locators.contact_menu).click()

    def click_about(self):
        self.find(locators.about_menu).click()

    def check_home_url_is_correct(self):
        return self.driver.current_url == self.home_url

    def check_news_url_is_correct(self):
        return self.driver.current_url == self.news_url

    def check_about_url_is_correct(self):
        return self.driver.current_url == self.about_url

    def check_contact_url_is_correct(self):
        return self.driver.current_url == self.contact_url
