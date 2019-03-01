from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement, MultiPageElement


class AndroidCalendarPageElement:

    btn_year_loc = (By.ID, 'mdtp_date_picker_year')
    btn_year = PageElement(btn_year_loc)

    txt_picker_day_loc = (By.ID, 'mdtp_date_picker_day')
    txt_picker_day = PageElement(txt_picker_day_loc)

    list_days_of_current_month_loc = (By.XPATH, '//*[@resource-id="com.anydo:id/mdtp_animator"]/android.support.v7.widget.RecyclerView[1]/android.view.View[1]/android.view.View')
    list_days_of_current_month = MultiPageElement(list_days_of_current_month_loc)

    btn_cancel_loc = (By.ID, 'mdtp_cancel')
    btn_cancel = PageElement(btn_cancel_loc)

    btn_ok_loc = (By.ID, 'mdtp_ok')
    btn_ok = PageElement(btn_ok_loc)

    list_years_loc = (By.XPATH, '//*[@resource-id="com.anydo:id/mdtp_animator"]/android.widget.ListView[1]/android.widget.TextView')
    list_years = MultiPageElement(list_years_loc)

    list_view_years_loc = (By.XPATH, '//*[@resource-id="com.anydo:id/mdtp_animator"]/android.widget.ListView[1]')
    list_view_years = PageElement(list_view_years_loc)

    month_calendar_loc = (By.XPATH, '//*[@resource-id="com.anydo:id/mdtp_animator"]/android.support.v7.widget.RecyclerView[1]/android.view.View[1]')
    month_calendar = PageElement(month_calendar_loc)

