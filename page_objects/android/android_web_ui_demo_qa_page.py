from page_object_elements.android.android_web_ui_demo_qa_elements import AndroidWebUiDemoQaPageElements
from page_objects.android.android_base_page import AndroidBasePage


class AndroidWebUiDemoQaPage(AndroidBasePage, AndroidWebUiDemoQaPageElements):
    def __init__(self, driver):
        super(AndroidWebUiDemoQaPage, self).__init__(driver)

    def search_for(self, text):
        qs = self.driver.find_element_by_class_name('android.widget.TextView')
        self.driver.set_value(qs, text)
        self.driver.get(text)