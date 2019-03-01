from selenium.webdriver.common.by import By
from lib.page_objects import PageElement, MultiPageElement


class CommonPageElements:
    # Defining locators and webelements.
    menu_admin_loc = (By.ID, "menu_admin_viewAdminModule")
    menu_admin = PageElement(menu_admin_loc)

    menu_pim_loc = (By.ID, "menu_pim_viewPimModule")
    menu_pim = PageElement(menu_pim_loc)

    menu_leave_loc = (By.ID, "menu_leave_viewLeaveModule")
    menu_leave = PageElement(menu_admin_loc)

    menu_time_loc = (By.ID, "menu_time_viewTimeModule")
    menu_time = PageElement(menu_time_loc)

    menu_recruitment_loc = (By.ID, "menu_recruitment_viewRecruitmentModule")
    menu_recruitment = PageElement(menu_recruitment_loc)

    menu_performance_loc = (By.ID, "menu__Performance")
    menu_performance = PageElement(menu_performance_loc)

    menu_dashboard_loc = (By.ID, "menu_dashboard_index")
    menu_dashboard = PageElement(menu_dashboard_loc)

    menu_directory_loc = (By.ID, "menu_directory_viewDirectory")
    menu_directory = PageElement(menu_directory_loc)

    # About Pop up
    btn_close_pop_up_loc = (By.XPATH, "//a[@class='close']")
    btn_close_pop_up = PageElement(btn_close_pop_up_loc)

    # Subsection
    menu_users_loc = (By.ID, "menu_admin_viewSystemUsers")
    menu_users = PageElement(menu_users_loc)

    menu_job_loc = (By.ID, "menu_admin_Job")
    menu_job = PageElement(menu_job_loc)

    menu_job_title_loc = (By.ID, "menu_admin_viewJobTitleList")
    menu_job_title = PageElement(menu_job_title_loc)

    menu_user_management_loc = (By.ID, "menu_admin_UserManagement")
    menu_user_management = PageElement(menu_user_management_loc)

    sel_user_options_loc = (By.XPATH, ".//*[@id='welcome-menu']/ul/li/a")
    sel_user_options = MultiPageElement(sel_user_options_loc)

    # Welcome user select menu
    sel_welcome_loc = (By.ID, "welcome")
    sel_welcome = PageElement(sel_welcome_loc)
    section_user_options_loc = (By.ID, "welcome-menu")
    section_user_options = PageElement(section_user_options_loc)

    btn_about_loc = (By.ID, "aboutDisplayLink")
    btn_about = PageElement(btn_about_loc)

    btn_change_password_loc = (By.XPATH, "//a[contains(.,'Change Password')]")
    btn_change_password = PageElement(btn_change_password_loc)

    btn_logout_loc = (By.XPATH, "//a[contains(.,'Logout')]")
    btn_logout = PageElement(btn_logout_loc)
