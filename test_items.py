from time import sleep


def test_page_contains_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    sleep(30)
    assert browser.find_element_by_xpath("//button[contains(@class, 'btn-add-to-basket')]")
