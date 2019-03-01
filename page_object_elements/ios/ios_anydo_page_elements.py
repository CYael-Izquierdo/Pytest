from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement


class IosAnydoPageElements:
    # DEFINING LOCATORS #

    # Test Locator
    btn_test_loc = (By.XPATH, "//a[@title='IOs Button']")
    btn_test = PageElement(btn_test_loc)