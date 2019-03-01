from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement, MultiPageElement


class MacCalculatorPageElements:
    window_path = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"

    window_loc = (By.XPATH, window_path)

    result_group_path = window_path + "/AXGroup[0]"
    result_group_loc = (By.XPATH, result_group_path)

    basic_group_path = window_path + "/AXGroup[1]"
    basic_group_loc = (By.XPATH, basic_group_path)

    scientific_group_path = window_path + "/AXGroup[2]"
    scientific_group_loc = (By.XPATH, scientific_group_path)

    programmer_group_path = window_path + "/AXGroup[1]"
    programmer_group_loc = (By.XPATH, programmer_group_path)

    menu_bar_ax_path = "/AXApplication[@AXTitle='Calculator']/AXMenuBar"
    menu_bar_ax_loc = (By.XPATH, menu_bar_ax_path)

    # DEFINING LOCATORS #
    # BY XPATH
    # Numbers
    btn_zero_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='zero']")
    btn_zero = PageElement(btn_zero_loc)

    btn_one_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='one']")
    btn_one = PageElement(btn_one_loc)

    btn_two_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='two']")
    btn_two = PageElement(btn_two_loc)

    btn_three_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='three']")
    btn_three = PageElement(btn_three_loc)

    btn_four_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='four']")
    btn_four = PageElement(btn_four_loc)

    btn_five_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='five']")
    btn_five = PageElement(btn_five_loc)

    btn_six_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='six']")
    btn_six = PageElement(btn_six_loc)

    btn_seven_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='seven']")
    btn_seven = PageElement(btn_seven_loc)

    btn_eight_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='eight']")
    btn_eight = PageElement(btn_eight_loc)

    btn_nine_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='nine']")
    btn_nine = PageElement(btn_nine_loc)

    # # Operations
    btn_add_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='add']")
    btn_add = PageElement(btn_add_loc)

    btn_sub_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='subtract']")
    btn_sub = PageElement(btn_sub_loc)

    btn_mul_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='multiply']")
    btn_mul = PageElement(btn_mul_loc)

    btn_div_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='divide']")
    btn_div = PageElement(btn_div_loc)

    # Close app
    btn_close_loc = (By.XPATH, window_path + "/AXCloseButton")
    btn_close = PageElement(btn_close_loc)

    # Equal
    btn_eq_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='equals']")
    btn_eq = PageElement(btn_eq_loc)

    # Result
    txt_result_loc = (By.XPATH, result_group_path + "/AXStaticText[@AXDescription='main display']")
    txt_result = PageElement(txt_result_loc)

    # clear
    btn_clear_loc = (By.XPATH, basic_group_path + "/AXButton[@AXDescription='clear']")
    btn_clear = PageElement(btn_clear_loc)
