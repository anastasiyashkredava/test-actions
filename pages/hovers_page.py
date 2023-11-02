from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.locators import hovers_page_locators as locators


class HoversPage(BasePage):
    page_url = '/hovers'

    def hover_an_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @property
    def all_elements(self):
        return self.find_all(locators.elements)

    def all_captions(self):
        return self.find_all(locators.captions)
