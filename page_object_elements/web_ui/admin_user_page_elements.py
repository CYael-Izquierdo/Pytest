from selenium.webdriver.common.by import By
from lib.page_objects import PageElement


class AdminUserPageElements:
    # Defining locators and webelements.
    txt_username_loc = (By.ID, "searchSystemUser_userName")
    txt_username = PageElement(txt_username_loc)

    sel_user_role_loc = (By.ID, "searchSystemUser_userType")
    sel_user_role = PageElement(sel_user_role_loc)

    txt_employee_name_loc = (By.ID, "searchSystemUser_employeeName_empName")
    txt_employee_name = PageElement(txt_employee_name_loc)

    txt_employee_name_id_loc = (By.ID, "searchSystemUser_userName")
    txt_employee_name_id = PageElement(txt_employee_name_id_loc)

    sel_status_loc = (By.ID, "searchSystemUser_status")
    sel_status = PageElement(sel_status_loc)

    btn_search_loc = (By.ID, "searchBtn")
    btn_search = PageElement(btn_search_loc)

    btn_reset_loc = (By.ID, "resetBtn")
    btn_reset = PageElement(btn_reset_loc)

    btn_add_job_loc = (By.ID, "btnAdd")
    btn_add_job = PageElement(btn_add_job_loc)

    btn_select_all_loc = (By.ID, "ohrmList_chkSelectAll")
    chk_select_all = PageElement(btn_select_all_loc)

    lbl_system_users_loc = (By.XPATH, "//div[@class='head']")
    lbl_system_users = PageElement(lbl_system_users_loc)

    tbl_user_search_result_loc = (By.XPATH, "//table[@id='resultTable']//tbody")
    tbl_user_search_result = PageElement(tbl_user_search_result_loc)

    user_links_loc = (By.LINK_TEXT, "username")

    
    "//table/tbody/tr/td[contains(.,'Enabled')]"
