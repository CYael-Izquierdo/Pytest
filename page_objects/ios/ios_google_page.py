from page_object_elements.ios.ios_google_page_element import IosGooglePageElement
from page_objects.ios.ios_base_page import IosBasePage


class IosGooglePage(IosGooglePageElement, IosBasePage):

    def search(self, txt_to_search):
        self.wait_for_element_to_be_present(self.txt_search_loc, waiting_time=5)
        self.driver.set_value(element=self.txt_search, value=txt_to_search)
        self.btn_search.click()

    def find_result(self, result_title):
        """

        :param result_title:
        :return: if it found a result return title WebElement if else return None
        """
        i = 0
        while i < 12:
            for title in self.result_titles_list:
                if title.text == result_title:
                    return title
            if self.is_visible(self.btn_more_results_loc):
                self.btn_more_results.click()
            self.scroll_down()
        return None
