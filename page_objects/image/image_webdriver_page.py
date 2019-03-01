from lib.image_based_testing.image_webdriver_handler import ImageWebdriverHandler
from page_objects.image.image_base_page import ImageBasePage
from lib.page_objects import PageObject


class ImageWebdriverPage(PageObject, ImageBasePage):

    def __init__(self, driver, class_name):
        ImageBasePage.__init__(self, class_name=class_name)
        PageObject.__init__(self, webdriver=driver)

        driver.save_screenshot(self.full_image_output_path)

        self.page_image = ImageWebdriverHandler(full_img_path=self.full_image_output_path,
                                                window_size=driver.get_window_size(),
                                                result_img_path=self.result_img_path)
