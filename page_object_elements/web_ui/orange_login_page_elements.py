from selenium.webdriver.common.by import By
from lib.page_objects import PageElement


class OrangeLoginPageElements:
    # Defining locators and webelements.
    txt_user_name_loc = (By.ID, "txtUsername")
    txt_user_name = PageElement(txt_user_name_loc)

    txt_password_loc = (By.ID, "txtPassword")
    txt_password = PageElement(txt_password_loc)

    btn_login_loc = (By.XPATH, "//input[@id='btnLogin']")
    btn_login = PageElement(btn_login_loc)

    login_panel_loc = (By.ID, "logInPanelHeading")
    login_panel = PageElement(login_panel_loc)
