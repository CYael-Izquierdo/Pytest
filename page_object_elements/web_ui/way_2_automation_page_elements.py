from selenium.webdriver.common.by import By
from lib.page_objects import PageElement


class Way2AutomationPageElements:
    img_logo_loc = (By.XPATH, r"//img[@src='demo/images/logo.png']")
    img_logo = PageElement(img_logo_loc)

    lbl_title_loc = (By.XPATH, r"//h1[contains(.,'Website for Testing Selenium / QTP scripts')]")
    lbl_title = PageElement(lbl_title_loc)

    block_registration_form_loc = (By.ID, r"load_box")
    block_registration_form = PageElement(block_registration_form_loc)

    txt_name_loc = (By.NAME, r"name")
    txt_name = PageElement(txt_name_loc)

    txt_phone_loc = (By.NAME, r"phone")
    txt_phone = PageElement(txt_phone_loc)

    txt_email_loc = (By.NAME, r"email")
    txt_email = PageElement(txt_email_loc)

    sel_country_loc = (By.NAME, r"country")
    sel_country = PageElement(sel_country_loc)

    txt_city_loc = (By.NAME, r"city")
    txt_city = PageElement(txt_city_loc)

    txt_username_loc = (By.XPATH, r"//div[@id='load_box']//input[@name='username']")
    txt_username = PageElement(txt_username_loc)

    txt_password_loc = (By.XPATH, r"//div[@id='load_box']//input[@name='password']")
    txt_password = PageElement(txt_password_loc)

    btn_submit_loc = (By.XPATH, r"//div[@id='load_box']//input[@type='submit']")
    btn_submit = PageElement(btn_submit_loc)

    # MENU #
    # <<<<Alert>>>>
    menu_alert_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Alert')]")
    menu_alert = PageElement(menu_alert_loc)

    # <<<<Registration>>>>
    menu_registration_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Registration')]")
    menu_registration = PageElement(menu_registration_loc)

    # <<<<Dynamic Elements>>>>
    menu_dynamic_elements_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Dynamic Elements')]")
    menu_dynamic_elements = PageElement(menu_dynamic_elements_loc)

    menu_submit_button_clicked_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Submit Button Clicked')]")
    menu_submit_button_clicked = PageElement(menu_submit_button_clicked_loc)
    menu_dropdown_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Dropdown')]")
    menu_dropdown = PageElement(menu_dropdown_loc)

    # <<<<Frames and Windows>>>>
    menu_frames_and_windows_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Frames and Window')]")
    menu_frames_and_windows = PageElement(menu_frames_and_windows_loc)

    # <<<<Widget>>>>
    menu_widget_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Widget')]")
    menu_widget = PageElement(menu_widget_loc)

    # <<<<Interaction>>>>
    menu_interaction_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Interaction')]")
    menu_interaction = PageElement(menu_interaction_loc)

    menu_draggable_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Draggable')]")
    menu_draggable = PageElement(menu_draggable_loc)

    menu_droppable_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Droppable')]")
    menu_droppable = PageElement(menu_droppable_loc)

    menu_resizable_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Resizable')]")
    menu_resizable = PageElement(menu_resizable_loc)

    menu_selectable_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Selectable')]")
    menu_selectable = PageElement(menu_selectable_loc)

    menu_sortable_loc = (By.XPATH, r"//div[@class='container main-nav']//a[contains(.,'Sortable')]")
    menu_sortable = PageElement(menu_sortable_loc)

    # ALERTS #
    btn_display_alert_loc = (By.XPATH, r"//body/button[@onclick='myFunction()']")
    btn_display_alert = PageElement(btn_display_alert_loc)
    tab_simple_alert_loc = (By.XPATH, r"//a[contains(.,'Simple Alert')]")
    tab_simple_alert = PageElement(tab_simple_alert_loc)
    tab_input_alert_loc = (By.XPATH, r"//a[contains(.,'Input Alert')]")
    tab_input_alert = PageElement(tab_input_alert_loc)

    # Dynamic Elements #
    tab_starts_with_loc = (By.XPATH, r"//a[contains(.,'Starts With')]")
    tab_starts_with = PageElement(tab_starts_with_loc)

    tab_ends_with_loc = (By.XPATH, r"//a[contains(.,'Ends With')]")
    tab_ends_with = PageElement(tab_ends_with_loc)

    tab_complete_id_dynamic_loc = (By.XPATH, r"//a[contains(.,'Complete id Dynamic')]")
    tab_complete_id_dynamic = PageElement(tab_complete_id_dynamic_loc)

    txt_form_input_loc = (By.XPATH, r"//input[@type='text']")
    txt_form_input = PageElement(txt_form_input_loc)

    btn_form_submit_loc = (By.XPATH, r"//input[@class='submit']")
    btn_form_submit = PageElement(btn_form_submit_loc)


