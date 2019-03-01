from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement, MultiPageElement


class AndroidAnydoPageElements:

    # DEFINING LOCATORS #

    # Add task button
    btn_add_task_loc = (By.ID, 'quick_add_button_container')
    btn_add_task = PageElement(btn_add_task_loc)

    # Go task button
    btn_task_loc = (By.ID, 'main_tabs_tasks')
    btn_task = PageElement(btn_task_loc)

    btn_later_today_loc = (By.XPATH, '//*[@text="Later today"]')
    btn_later_today = PageElement(btn_later_today_loc)

    btn_this_evening_loc = (By.XPATH, '//*[@text="This evening"]')
    btn_this_evening = PageElement(btn_this_evening_loc)

    btn_tomorrow_morning_loc = (By.XPATH, '//*[@text="Tomorrow morning"]')
    btn_tomorrow_morning = PageElement(btn_tomorrow_morning_loc)

    btn_next_week_loc = (By.XPATH, '//*[@text="Next week"]')
    btn_next_week = PageElement(btn_next_week_loc)

    btn_someday_loc = (By.XPATH,
                       '//*[@resource-id="com.anydo:id/quickAddOptionButtonsContainer"]/android.widget.CheckBox[@text="Someday"]')
    btn_someday = PageElement(btn_someday_loc)

    btn_custom_loc = (By.XPATH, '//*[@text="Custom"]')
    btn_custom = PageElement(btn_custom_loc)

    btn_confirm_task_loc = (By.ID, 'quick_add_button_container')
    btn_confirm_task = PageElement(btn_confirm_task_loc)

    bar_day_loc = (By.ID, 'quickAddOptionContainer')
    bar_day = PageElement(bar_day_loc)

    btn_delete_task_loc = (By.ID, 'deleteTaskButton')
    btn_delete_task = PageElement(btn_delete_task_loc)

    list_tasks_loc = (By.ID, 'title')
    list_tasks = MultiPageElement(list_tasks_loc)

    txt_task_title_loc = (By.ID, 'quick_add_input')
    txt_task_title = PageElement(txt_task_title_loc)

    task_detail_loc = (By.ID, 'taskDetailsRecycler')
    task_detail = PageElement(task_detail_loc)

    btn_true_delete_button_loc = (By.ID, 'deleteButton')
    btn_true_delete_button = PageElement(btn_true_delete_button_loc)

    btn_keep_editing_loc = (By.ID, 'keepEditingButton')
    btn_keep_editing = PageElement(btn_keep_editing_loc)
