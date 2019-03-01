from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement


class AndroidChromePageElements:
    # DEFINING LOCATORS #
    # BY XPATH

    btn_terms_accept_loc= (By.ID, r"com.android.chrome:id/terms_accept")
    btn_terms_accept = PageElement(btn_terms_accept_loc)

    btn_terms_accept_next_loc = (By.ID, r"com.android.chrome:id/next_button")
    btn_terms_accept_next = PageElement(btn_terms_accept_next_loc)

    btn_negative_loc = (By.ID, r"com.android.chrome:id/negative_button")
    btn_negative = PageElement(btn_negative_loc)

    btn_no_thanks_loc = (By.ID, r"com.android.chrome:id/negative_button")
    btn_no_thanks = PageElement(btn_no_thanks_loc)

