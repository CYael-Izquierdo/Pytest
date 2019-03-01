from assertpy import assert_that
from page_objects.image.image_webdriver_page import ImageWebdriverPage
from page_object_elements.image.redmine.home_page.redmine_homepage_by_image_page_elements import \
    RedmineHomepageByImagePagePageElements


class RedmineHomepageByImagePage(ImageWebdriverPage, RedmineHomepageByImagePagePageElements):

    def __init__(self, driver, uri=None):
        super(RedmineHomepageByImagePage, self).__init__(driver, RedmineHomepageByImagePage.__name__)
        self.url = uri

        # Comparing home screenshot against standard image
        assert_that(self.page_image.find_img_on_screen(target_img_path=self.full_image_output_path,
                                                       full_img_path=self.home_page_standard_path[1],
                                                       draw_rectangle=True)).described_as(
            "Home Page screenshot does not match with the standard image: " + "\n" +
            "Standard image: " + self.home_page_standard_path[1] + "\n" +
            "Screenshot image: " + self.full_image_output_path).\
            is_true()

    def click_on_link(self, link_name: str):
        if link_name.upper() == "SIGN IN":
            self.btn_sign_in.click()
