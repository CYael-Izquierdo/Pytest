from page_object_elements.mac_desktop.mac_calculator_page_elements import MacCalculatorPageElements
from page_objects.ios.ios_base_page import IosBasePage
import time


class MacCalculatorPage(IosBasePage, MacCalculatorPageElements):

    def __init__(self, driver):
        super(MacCalculatorPage, self).__init__(driver)

    def add_two_values(self, op_a, op_b, operation):
        self.wait_for_element_to_be_present(element_locator=self.basic_group_loc, waiting_time=10)
        self.btn_clear.click()
        self.click_on_calc_number(op_a)
        self.click_on_operation(operation)
        self.click_on_calc_number(op_b)
        self.btn_eq.click()

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

    def get_calculator_result(self):
        self.wait_for_element_to_be_present(element_locator=self.txt_result_loc, waiting_time=10)
        return self.txt_result.text

    def close_mac_desktop_calculator(self):
        self.btn_close.click()

