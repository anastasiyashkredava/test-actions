from pages.hovers_page import HoversPage


def test_text_appear_on_hovering(driver):
    hovers_page = HoversPage(driver)
    hovers_page.open()
    all_elements = hovers_page.all_elements
    all_captions = hovers_page.all_captions()
    for index, element in enumerate(all_elements):
        hovers_page.hover_an_element(element)
        assert all_captions[index].is_displayed()
