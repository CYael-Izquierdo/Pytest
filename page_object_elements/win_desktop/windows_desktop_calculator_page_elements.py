from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement


class WindowsDesktopCalculatorPageElements:
    # DEFINING LOCATORS #
    # BY XPATH
    # Numbers
    btn_zero_loc = (By.NAME, r"Zero")
    btn_zero = PageElement(btn_zero_loc)

    btn_one_loc = (By.NAME, r"One")
    btn_one = PageElement(btn_one_loc)

    btn_two_loc = (By.NAME, r"Two")
    btn_two = PageElement(btn_two_loc)

    btn_three_loc = (By.NAME, r"Three")
    btn_three = PageElement(btn_three_loc)

    btn_four_loc = (By.NAME, r"Four")
    btn_four = PageElement(btn_four_loc)

    btn_five_loc = (By.NAME, r"Five")
    btn_five = PageElement(btn_five_loc)

    btn_six_loc = (By.NAME, r"Six")
    btn_six = PageElement(btn_six_loc)

    btn_seven_loc = (By.NAME, r"Seven")
    btn_seven = PageElement(btn_seven_loc)

    btn_eight_loc = (By.NAME, r"Eight")
    btn_eight = PageElement(btn_eight_loc)

    btn_nine_loc = (By.NAME, r"Nine")
    btn_nine = PageElement(btn_nine_loc)

    # # Operations
    btn_add_loc = (By.NAME, r"Plus")
    btn_add = PageElement(btn_add_loc)

    btn_sub_loc = (By.NAME, r"Minus")
    btn_sub = PageElement(btn_sub_loc)

    btn_mult_loc = (By.NAME, r"Multiply by")
    btn_mult = PageElement(btn_mult_loc)

    btn_div_loc = (By.NAME, r"Divide by")
    btn_div = PageElement(btn_div_loc)

    btn_equ_loc = (By.NAME, r"Equals")
    btn_equ = PageElement(btn_equ_loc)

    btn_clear_loc = (By.NAME, r"Clear")
    btn_clear = PageElement(btn_clear_loc)

    # Result
    txt_result_loc = (By.ACCESSIBILITY_ID, r"CalculatorResults")
    # txt_result_loc = (By.NAME, r"Main Display")
    txt_result = PageElement(txt_result_loc)


