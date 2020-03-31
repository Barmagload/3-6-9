#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_the_button(browser):
    browser.get(link)
    #time.sleep(30)
    button = len(browser.find_elements_by_class_name("btn-primary"))

    assert button > 0, 'No button =('
