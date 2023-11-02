from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.locators import drag_and_drop_page_locators as locators


class DragAndDropPage(BasePage):
    page_url = '/drag_and_drop'

    @property
    def the_first_square(self):
        return self.find(locators.the_first_square)

    @property
    def the_second_square(self):
        return self.find(locators.the_second_square)

    def check_default_squares_names(self):
        return self.the_first_square.text == 'A' and self.the_second_square.text == 'B'

    def check_squares_names_after_drag_and_drop(self):
        return self.the_first_square.text == 'B' and self.the_second_square.text == 'A'

    def drag_the_first_square_to_the_second(self):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(self.the_first_square, self.the_second_square).perform()
