from page_objects.ios.ios_base_page import IosBasePage
from page_objects.android.android_base_page import AndroidBasePage
from page_object_elements.android.android_anydo_page_elements import AndroidAnydoPageElements
from page_object_elements.ios.ios_anydo_page_elements import IosAnydoPageElements


class AnydoPageObject(IosBasePage, AndroidBasePage):
    pe = None

    def __init__(self, driver):
        super(AnydoPageObject, self).__init__(driver)
        self.is_android_test = self.is_android_test()
        self.is_ios_test = self.is_ios_test()

        if self.is_android_test:
            AnydoPageObject.pe = AndroidAnydoPageElements
        elif self.is_ios_test:
            AnydoPageObject.pe = IosAnydoPageElements
        else:
            raise Exception (
            4 * "<" + "[ERROR]" + 4 * ">"
            + "\nERROR: "
            + "This is not an mobile test. Class:  " + "AnydoPageObject"
            + "\n")

    def print_test(self):
        print("********PAGE ELEMENT: " + self.pe.btn_test_loc[1])
