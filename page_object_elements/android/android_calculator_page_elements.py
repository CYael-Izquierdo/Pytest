from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement, MultiPageElement


class AndroidCalculatorPageElements:
    # DEFINING LOCATORS #
    # BY XPATH
    # Numbers
    emu_current_package = "com.android.calculator2"
    rd_current_package = "com.google.android.calculator"

    btn_zero_loc = (By.XPATH, r"//android.widget.Button[@text='0']")
    btn_zero = PageElement(btn_zero_loc)

    btn_one_loc = (By.XPATH, r"//android.widget.Button[@text='1']")
    btn_one = PageElement(btn_one_loc)

    btn_two_loc = (By.XPATH, r"//android.widget.Button[@text='2']")
    btn_two = PageElement(btn_two_loc)

    btn_three_loc = (By.XPATH, r"//android.widget.Button[@text='3']")
    btn_three = PageElement(btn_three_loc)

    btn_four_loc = (By.XPATH, r"//android.widget.Button[@text='4']")
    btn_four = PageElement(btn_four_loc)

    btn_five_loc = (By.XPATH, r"//android.widget.Button[@text='5']")
    btn_five = PageElement(btn_five_loc)

    btn_six_loc = (By.XPATH, r"//android.widget.Button[@text='6']")
    btn_six = PageElement(btn_six_loc)

    btn_seven_loc = (By.XPATH, r"//android.widget.Button[@text='7']")
    btn_seven = PageElement(btn_seven_loc)

    btn_eight_loc = (By.XPATH, r"//android.widget.Button[@text='8']")
    btn_eight = PageElement(btn_eight_loc)

    btn_nine_loc = (By.XPATH, r"//android.widget.Button[@text='9']")
    btn_nine = PageElement(btn_nine_loc)

    # # Operations
    btn_add_loc = (By.XPATH, r"//android.widget.Button["
                             r"@resource-id='" + emu_current_package + ":id/op_add' or" r"@resource-id='" + rd_current_package + ":id/op_add']")
    btn_add = PageElement(btn_add_loc)

    btn_sub_loc = (By.XPATH, r"//android.widget.Button[@resource-id='" + emu_current_package + ":id/op_sub' or" r"@resource-id='" + rd_current_package + ":id/op_sub']")
    btn_sub = PageElement(btn_sub_loc)

    btn_div_loc = (By.XPATH, r"//android.widget.Button[@resource-id='" + emu_current_package + ":id/op_div' or" r"@resource-id='" + rd_current_package + ":id/op_div']")
    btn_div = PageElement(btn_div_loc)

    btn_mul_loc = (By.XPATH, r"//android.widget.Button[@resource-id='" + emu_current_package + ":id/op_mul' or" r"@resource-id='" + rd_current_package + ":id/op_mul']")
    btn_mul = PageElement(btn_mul_loc)

    btn_equ_loc = (By.XPATH, r"//android.widget.Button[@text='=']")
    btn_equ = PageElement(btn_equ_loc)

    btn_del_loc = (By.XPATH, r"//android.widget.Button[@resource-id='" + emu_current_package + ":id/del' or" r"@resource-id='" + rd_current_package + ":id/del']")
    btn_del = PageElement(btn_del_loc)

    # Result
    txt_result_loc = (By.XPATH, r"//android.widget.TextView[contains(@resource-id,'id/result')]")
    txt_result = PageElement(txt_result_loc)

    # Other Examples
    # By UIAutomation
    btn_zero_ui_automation_loc = (By.ANDROID_UIAUTOMATOR, r'new UiSelector().resourceId("com.android.calculator2:id/digit_0")')
    btn_zero_ui_automation = PageElement(btn_zero_ui_automation_loc)
    btn_one_ui_automation_loc = (By.ANDROID_UIAUTOMATOR, r'new UiSelector().resourceId("com.android.calculator2:id/digit_1")')
    btn_one_ui_automation = PageElement(btn_one_ui_automation_loc)

    # By CLASS NAME
    btn_two_class_name_loc = (By.CLASS_NAME, "android.widget.Button")
    btn_two_class_name = MultiPageElement(btn_two_class_name_loc)

    # By ID
    btn_three_id_loc = (By.ID, r"com.android.calculator2:id/digit_3")
    btn_three_id = PageElement(btn_three_id_loc)

    # By Accessibility ID
    btn_delete_accessibility_id_loc = (By.ACCESSIBILITY_ID, r"delete")
    btn_delete_accessibility_id = PageElement(btn_delete_accessibility_id_loc)

    # Advanced operations
    btn_advanced_op_accessibility_id_loc = (By.ACCESSIBILITY_ID, r"Advanced operations")
    btn_advanced_op_accessibility_id = PageElement(btn_advanced_op_accessibility_id_loc)
