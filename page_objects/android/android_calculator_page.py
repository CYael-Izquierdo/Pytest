from page_object_elements.android.android_calculator_page_elements import AndroidCalculatorPageElements
from page_objects.android.android_base_page import AndroidBasePage
import time


class AndroidCalculatorPage(AndroidBasePage, AndroidCalculatorPageElements):

    def __init__(self, driver):
        super(AndroidCalculatorPage, self).__init__(driver)
        previous_package = AndroidCalculatorPageElements.emu_current_package
        import inspect
        page_el_properties = inspect.getmembers(AndroidCalculatorPageElements, lambda a: not (inspect.isroutine(a)))
        for p in page_el_properties:

            if p[0] == "current_package":
                AndroidCalculatorPageElements.emu_current_package = self.driver.current_package

    def sum_two_values(self, td):
        a, b = td.get("operation").split("+")

        # TODO: Workaround for MotoG which opens calculator with the advance operation section opened.
        # I haven't found a expected condition for a webdriver wait or appWaitActivity appium capability
        # to replace this sleep.
        time.sleep(2)
        # End Workaround

        self.click_on_calc_number(a)
        self.btn_add.click()
        self.click_on_calc_number(b)
        self.btn_equ.click()

    def calculate(self, op_a, op_b, operation):
        # TODO: Workaround for MotoG which opens calculator with the advance operation section opened.
        # I haven't found a expected condition for a webdriver wait or appWaitActivity appium capability
        # to replace this sleep.
        time.sleep(2)
        # End Workaround

        self.click_on_calc_number(op_a)
        self.click_on_operation(operation)
        self.click_on_calc_number(op_b)
        self.btn_equ.click()

    # For testing purpose
    def sum_two_values_by_other_methods(self):
        # Testing ui automation locator
        self.btn_one_ui_automation.click()

        # Testing class name locator
        self.btn_two_class_name[16].click()

        # Testing id locator
        self.btn_three_id.click()

        # Testing Accesibilit ID (content desc)
        self.btn_delete_accessibility_id.click()

    def click_number(self, num):
        if num == "0":
            self.btn_zero.click()
        elif num == "1":
            self.btn_one.click()
        elif num == "2":
            self.btn_two.click()
        elif num == "3":
            self.btn_three.click()
        elif num == "4":
            self.btn_four.click()
        elif num == "5":
            self.btn_five.click()
        elif num == "6":
            self.btn_six.click()
        elif num == "7":
            self.btn_seven.click()
        elif num == "8":
            self.btn_eight.click()
        elif num == "9":
            self.btn_nine.click()

    def click_on_calc_number(self, value):
        for v in value:
            self.click_number(v)

    def click_on_operation(self, op):
        if op.upper() == "PLUS":
            self.btn_add.click()
        elif op.upper() == "SUBTRACTION":
            self.btn_sub.click()
        elif op.upper() == "DIVISION":
            self.btn_div.click()
        elif op.upper() == "MULTIPLICATION":
            self.btn_mul.click()

    # Get result from calculator display
    def get_result(self):
        self.wait_for_element_to_be_present(element_locator=self.txt_result_loc, waiting_time=10)
        return self.txt_result.text
