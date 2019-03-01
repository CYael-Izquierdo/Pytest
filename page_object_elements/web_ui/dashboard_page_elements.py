from selenium.webdriver.common.by import By
from lib.page_objects import PageElement


class DashboardPageElements:
    # Defining locators and webelements.
    dashboard_title_loc = (By.XPATH, "//h1[contains(.,'Dashboard')]")
    lbl_dashboard_title = PageElement(dashboard_title_loc)

    user_name_loc = (By.ID, "txtUsername")
    txt_user_name = PageElement(user_name_loc)

    lnk_assign_leave_loc = (By.LINK_TEXT, "Assign Leave")
    lnk_assign_leave = PageElement(lnk_assign_leave_loc)

    lnk_leave_list_loc = (By.LINK_TEXT, "Leave List")
    lnk_leave_list = PageElement(lnk_leave_list_loc)

    lnk_timesheets_loc = (By.LINK_TEXT, "Timesheets")
    lnk_timesheets = PageElement(user_name_loc)

    img_assign_leave_loc = (By.XPATH, "//img[contains(@src,'ApplyLeave.png')]")
    img_assign_leave = PageElement(img_assign_leave_loc)

    img_leave_list_loc = (By.XPATH, "//img[contains(@src,'MyLeave.png')]")
    img_leave_list = PageElement(img_leave_list_loc)

    img_timesheets_loc = (By.XPATH, "//img[contains(@src,'MyTimesheet.png')]")
    img_timesheets = PageElement(user_name_loc)

    lbl_welcome_loc = (By.ID, "welcome")
    lbl_welcome = PageElement(lbl_welcome_loc)
