from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement, MultiPageElement


class AndroidBelaxElements:
    # DEFINING LOCATORS #

    # Contact Header Button
    btn_contact_header_loc = (By.XPATH, "//a[@title='Contact Us']")
    btn_contact_header = PageElement(btn_contact_header_loc)

    # Contact us Button
    btn_contact_us_loc = (By.XPATH, "//android.view.View[@content-desc='Contact Us Contact Us']")
    btn_contact_us = PageElement(btn_contact_us_loc)

    txt_first_name_loc = (By.XPATH, "//android.widget.EditText[@resource-id='form_0036_fld_0_fn']")
    txt_first_name = PageElement(txt_first_name_loc)

    txt_last_name_loc = (By.XPATH, "//android.widget.EditText[@resource-id='form_0036_fld_0_ln']")
    txt_last_name = PageElement(txt_last_name_loc)

    txt_email_loc = (By.XPATH, "//android.widget.EditText[@resource-id='form_0036_fld_1']")
    txt_email = PageElement(txt_email_loc)

    txt_phone_loc = (By.XPATH, "//android.widget.EditText[@resource-id='form_0036_fld_2']")
    txt_phone = PageElement(txt_phone_loc)

    sel_service_loc = (By.XPATH, "//android.widget.EditText[@resource-id='form_0036_fld_3']")
    sel_service = PageElement(sel_service_loc)

    txt_description_loc = (By.XPATH, "//android.widget.EditText[@resource-id='form_0036_fld_4']")
    txt_description = PageElement(txt_description_loc)

    btn_submit_loc = (By.XPATH, "//android.view.View[@resource-id='form_0036_ao_submit_href']")
    btn_submit = PageElement(btn_submit_loc)

    lbl_message_sent_loc = (By.XPATH, "//android.view.View[@content-desc='Thanks for your request!']")
    lbl_message_sent = PageElement(lbl_message_sent_loc)


