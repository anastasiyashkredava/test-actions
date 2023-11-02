from pages.floating_menu_page import FloatingMenuPage


def test_floating_menu(driver):
    floating_menu_page = FloatingMenuPage(driver)
    floating_menu_page.open()
    floating_menu_page.scroll()
    floating_menu_page.click_home()
    assert floating_menu_page.check_home_url_is_correct()
    floating_menu_page.click_news()
    assert floating_menu_page.check_news_url_is_correct()
    floating_menu_page.click_about()
    assert floating_menu_page.check_about_url_is_correct()
    floating_menu_page.click_contact()
    assert floating_menu_page.check_contact_url_is_correct()
