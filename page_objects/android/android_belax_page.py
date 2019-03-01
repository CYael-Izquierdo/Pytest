from page_objects.android.android_base_page import AndroidBasePage
from page_object_elements.android.android_belax_elements import AndroidBelaxElements


class AndroidBelaxAPage(AndroidBasePage, AndroidBelaxElements):

    # Define constructor and methods.
    def __init__(self, driver):
        super(AndroidBelaxAPage, self).__init__(driver)

    def contact_us(self):
        pass
        self.wait_for_element_to_be_present(element_locator=self.btn_contact_header_loc,
                                            waiting_time=60)
        self.btn_contact_header.click()

        self.btn_contact_us.click()
        self.wait_for_element_to_be_present(element_locator=self.txt_first_name_loc,
                                            waiting_time=60)
        self.txt_first_name = "Fake name"
        self.txt_last_name = "Fake last name"
        self.txt_email = "fakeemail@fakehost.com"
        self.txt_phone = "2255442266"
        # self.txt_company = "CoE"
        self.sel_service = "Looking for a job"
        self.btn_submit.click()
