from assertpy import assert_that
from page_object_elements.image.redmine.login_page.redmine_login_by_image_page_elements import RedmineLoginByImagePagePageElements
from page_objects.image.image_webdriver_page import ImageWebdriverPage


class RedmineLoginByImagePage(ImageWebdriverPage, RedmineLoginByImagePagePageElements):

    # Define constructor and methods.
    def __init__(self, driver, uri=None):
        super(RedmineLoginByImagePage, self).__init__(driver, RedmineLoginByImagePage.__name__)
        self.url = uri

        # Comparing home screenshot against standard image
        self.page_image.set_threshold(0.85)
        assert_that(self.page_image.find_img_on_screen(target_img_path=self.full_image_output_path,
                                                       full_img_path=self.login_page_standard_path[1],
                                                       draw_rectangle=True)).described_as(
            "Login Page screenshot does not match with the standard image: " + "\n" +
            "Standard image: " + self.login_page_standard_path[1] + "\n" +
            "Screenshot image: " + self.full_image_output_path).\
            is_true()

        self.page_image.set_threshold(0.99)

    def login(self, username: str, password: str):
        self.txt_login_in = username
        self.txt_password = password
        self.btn_login.submit()
