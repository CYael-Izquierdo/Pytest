from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement, MultiPageElement


class IosReminderPageElements:
    # Locator examples:
    btn = (By.ACCESSIBILITY_ID, r"Add")
    btn_loc = (By.XPATH, r"//*[@name='Add']")
    btn_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]")

    # DEFINING LOCATORS #
    # BY XPATH
    # + button
    # btn_add_loc = (By.ACCESSIBILITY_ID, r"Add")
    # btn_add_loc = (By.XPATH, r"//*[@name='Add']")
    btn_add_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]")
    btn_add = PageElement(btn_add_loc)

    # Add reminder option
    btn_add_reminder_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeSheet[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]")
    # btn_add_reminder_loc = (By.ACCESSIBILITY_ID, r"")
    btn_add_reminder = PageElement(btn_add_reminder_loc)

    # Add list option
    # btn_add_list_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeSheet[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton[1]")
    btn_add_list_loc = (By.ACCESSIBILITY_ID, r"List")
    btn_add_list = PageElement(btn_add_list_loc)

    # Search
    # txt_search_reminder_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSearchField[1]")
    txt_search_reminder_loc = (By.ACCESSIBILITY_ID, r"Search")
    txt_search_reminder = PageElement(txt_search_reminder_loc)

    # Cancel
    btn_cancel_loc = (By.ACCESSIBILITY_ID, r"Cancel")
    # btn_cancel_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeSheet[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]")
    btn_cancel = PageElement(btn_cancel_loc)

    # Schedule tab
    btn_schedule_tab_loc = (By.ACCESSIBILITY_ID, r"Scheduled")
    # btn_schedule_tab_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeButton[1]")
    btn_schedule_tab = PageElement(btn_schedule_tab_loc)

    # Reminder tab
    btn_reminder_tab_loc = (By.ACCESSIBILITY_ID, r"Reminders")
    # btn_reminder_tab_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeButton[2]")
    btn_reminder_tab = PageElement(btn_reminder_tab_loc)

    # Back
    btn_back_loc = (By.ACCESSIBILITY_ID, r"Stack of other lists")
    # btn_back_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeButton[2]")
    btn_back = PageElement(btn_back_loc)

    # New Reminder
    btn_new_reminder_loc = (By.ACCESSIBILITY_ID, r"New reminder")
    # btn_new_reminder_loc = (By.XPATH, r"// XCUIElementTypeApplication[1] / XCUIElementTypeWindow[1] / XCUIElementTypeOther[1] / XCUIElementTypeOther[1] / \
    #    XCUIElementTypeScrollView[1] / XCUIElementTypeButton[1] / XCUIElementTypeOther[2] / XCUIElementTypeTable[1] / \
    #    XCUIElementTypeOther[1] / XCUIElementTypeTextView[1]")
    btn_new_reminder = PageElement(btn_new_reminder_loc)

    # More Info
    btn_more_info_loc = (By.ACCESSIBILITY_ID, r"More Info")
    # btn_more_info_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeButton[1]/XCUIElementTypeOther[2]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]")
    btn_more_info = PageElement(btn_more_info_loc)

    # >>>>>>>>>>>>>><

    # Done
    btn_done_loc = (By.ACCESSIBILITY_ID, r"Done")
    # btn_done_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeNavigationBar[1]/XCUIElementTypeButton[1]")
    btn_done = PageElement(btn_done_loc)

    # Reminder Title
    txt_reminder_title_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeTextView[1]")
    txt_reminder_title = PageElement(txt_reminder_title_loc)

    # Remind me day
    btn_reminder_day_loc = (By.ACCESSIBILITY_ID, r"Remind me on a day")
    # btn_reminder_day_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeSwitch[1]")
    btn_reminder_day = PageElement(btn_reminder_day_loc)

    # Priority None
    btn_priority_none_loc = (By.ACCESSIBILITY_ID, r"None")
    # btn_priority_none_loc = (By.XPATH, r"//*[@name='None']")
    btn_priority_none = PageElement(btn_priority_none_loc)

    # Priority !
    btn_priority_low_loc = (By.ACCESSIBILITY_ID, r"Low")
    btn_priority_low = PageElement(btn_priority_low_loc)

    # Priority !!
    btn_priority_medium_loc = (By.ACCESSIBILITY_ID, r"Medium")
    btn_priority_medium = PageElement(btn_priority_medium_loc)

    # Priority !!!
    btn_priority_high_loc = (By.ACCESSIBILITY_ID, r"High")
    btn_priority_high= PageElement(btn_priority_high_loc)

    # Reminder Notes
    # txt_reminder_notes_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[4]/XCUIElementTypeTextView[1]")
    # txt_reminder_notes_loc = (By.XPATH, r"(// XCUIElementTypeTextView)[last()]")
    txt_reminder_notes_loc = (By.XPATH, r"(//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]//XCUIElementTypeTextView)[last()]")
    txt_reminder_notes = PageElement(txt_reminder_notes_loc)



    # Reminder
    btn_reminder_loc = (By.XPATH, r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeButton[2]")
    btn_reminder = PageElement(btn_reminder_loc)

    # Reminder search result
    block_reminder_list_loc = (By.XPATH,
                           r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]")

    block_reminder_list = PageElement(block_reminder_list_loc)

    # First search result
    first_search_result_loc = (By.XPATH,
                               r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]")
    first_search_result = PageElement(first_search_result_loc)

    # First Reminder
    first_reminder_loc = (By.XPATH,
                                # r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeButton[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]")
                                r"//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeButton[1]/XCUIElementTypeOther[2]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]")
    first_reminder = PageElement(first_reminder_loc)




