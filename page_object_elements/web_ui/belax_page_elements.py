from selenium.webdriver.common.by import By
from lib.page_objects import PageElement, MultiPageElement


class BelaxPageElements:
    # Defining locators and webelements.
    lnk_contact_loc = (By.XPATH, "//div[@id='bs-example-navbar-collapse-1']//a[@title='Contact Us']")
    lnk_contact = PageElement(lnk_contact_loc)

    txt_first_name_loc = (By.XPATH, "//input[@name='FirstName']")
    txt_first_name = PageElement(txt_first_name_loc)

    txt_last_name_loc = (By.XPATH, "//input[@name='LastName']")
    txt_last_name = PageElement(txt_last_name_loc)

    txt_email_loc = (By.XPATH, "//input[@name='Email']")
    txt_email = PageElement(txt_email_loc)

    txt_phone_loc = (By.XPATH, "//input[@name='Phone']")
    txt_phone = PageElement(txt_phone_loc)

    txt_company_loc = (By.XPATH, "//input[@name='Company']")
    txt_company = PageElement(txt_company_loc)

    sel_service_loc = (By.XPATH, "//select[@name='ServicesNeeded']")
    sel_service = PageElement(sel_service_loc)

    txt_description_loc = (By.XPATH, "//textarea[@name='Description']")
    txt_description = PageElement(txt_description_loc)

    btn_submit_loc = (By.XPATH, "//button[@type='submit']")
    btn_submit = PageElement(btn_submit_loc)

    lbl_message_sent_loc = (By.XPATH, "//h2[contains(.,'Thanks for your request!')]")
    lbl_message_sent = PageElement(lbl_message_sent_loc)
