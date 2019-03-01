from page_objects.android.android_base_page import AndroidBasePage
from page_object_elements.android.android_chrome_page_elements import AndroidChromePageElements


class ChromePage(AndroidBasePage, AndroidChromePageElements):

    def __init__(self, driver):
        super(ChromePage, self).__init__(driver)

    def accept_chrome_conditions(self):
        try:
            self.wait_for_element_to_be_present(self.btn_terms_accept_loc, waiting_time=5)
            self.btn_terms_accept.click()
            try:
                self.wait_for_element_to_be_present( self.btn_terms_accept_next_loc, waiting_time=5)
                self.btn_terms_accept_next.click()
            except Exception:
                print("Next button is not present.")

            self.wait_for_element_to_be_present(self.btn_negative_loc, waiting_time=5)
            self.btn_negative.click()
        except Exception:
            print("Not able to accept Google Chrome terms and conditions.")
