from pages.drag_and_drop_page import DragAndDropPage


def test_squares_names(driver):
    drag_and_drop_page = DragAndDropPage(driver)
    drag_and_drop_page.open()
    assert drag_and_drop_page.check_default_squares_names()
    drag_and_drop_page.drag_the_first_square_to_the_second()
    assert drag_and_drop_page.check_squares_names_after_drag_and_drop()
