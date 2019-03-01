from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement, MultiPageElement


class IosCalendarPageElement:

    # DEFINING LOCATORS #

    # Button for a higher view of calendar
    btn_higher_view_loc = (By.XPATH,
                           r'//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeNavigationBar[1]/XCUIElementTypeButton[1]')
    btn_higher_view = PageElement(btn_higher_view_loc)

    # Button for a lower view of calendar
    btn_lower_view_loc = (By.ACCESSIBILITY_ID, r"Today")
    btn_lower_view = PageElement(btn_lower_view_loc)

    # Date
    txt_date_loc = (By.XPATH,
                    r'//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]')
    txt_date = PageElement(txt_date_loc)

    # Calendar Button
    btn_calendar_loc = (By.XPATH,
                        r'//*[@name="Toolbar"]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]')
    btn_calendar = PageElement(btn_calendar_loc)

    # Inbox button
    btn_inbox_loc = (By.ACCESSIBILITY_ID, r'Inbox')
    btn_inbox = PageElement(btn_inbox_loc)

    # year element in year view
    txt_year_yv_loc = (By.XPATH,
                       '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]')
    txt_year_yv = PageElement(txt_year_yv_loc)

