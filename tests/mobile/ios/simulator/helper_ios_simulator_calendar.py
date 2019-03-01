from page_objects.ios.ios_calendar_page import IosCalendarPage


def slice_in_day_view(direction: str, driver):
    calendar_po = IosCalendarPage(driver)
    calendar_po.go_to_day_view()
    if direction == 'right':
        calendar_po.slide_right()
    elif direction == 'left':
        calendar_po.slide_left()
