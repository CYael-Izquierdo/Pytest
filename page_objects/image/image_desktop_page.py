from page_objects.image.image_base_page import ImageBasePage
from lib import util
from lib.image_based_testing.image_desktop_handler import ImageDesktopHandler


class ImageDesktopPage(ImageBasePage):

    def __init__(self, class_name):
        super(ImageDesktopPage, self).__init__(class_name)

        self.page_image = ImageDesktopHandler(full_img_path=self.full_image_output_path,
                                              result_img_path=self.result_img_path)

    @staticmethod
    def wait(waiting_time):
        import time
        time.sleep(waiting_time)