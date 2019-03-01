from lib.page_objects import PageObject
from lib import util


class ImageBasePage(object):

    def __init__(self, class_name):
        self.screenshot_output_folder_path = util.get_proyect_root_path() + \
                                             util.read_config_file("behave.ini")["behave"]["images_output_path"]
        self.screenshot_file_name = class_name.lower() + "_SCREENSHOT" + ".png"
        self.full_image_output_path = self.screenshot_output_folder_path + self.screenshot_file_name

        self.result_img_path = self.screenshot_output_folder_path + class_name + "_MATCHING_RESULT" + ".png"
