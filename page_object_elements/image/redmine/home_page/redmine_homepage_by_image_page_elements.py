from appium.webdriver.common.mobileby import MobileBy as By
from lib.page_objects import ImageWebdriverPageElement
from lib import util


class RedmineHomepageByImagePagePageElements:
    __project_root_path = util.get_proyect_root_path()
    browser_image_path = __project_root_path + "/reports/visual_image_testing/RedmineHomepageByImagePage_SCREENSHOT.png"

    # Home Standard Image
    home_page_standard_path = (By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/home_page/standard/home_page.png",
                               browser_image_path)
    home_page_image = ImageWebdriverPageElement(home_page_standard_path)

    # Sign in Locator
    btn_sign_in_path = (By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/home_page/target/sign_in_btn.png",
                        browser_image_path)

    btn_sign_in = ImageWebdriverPageElement(btn_sign_in_path)

    # Register Locator
    btn_register_path = (
        By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/home_page/target/register_btn.png",
        browser_image_path)

    btn_register = ImageWebdriverPageElement(btn_register_path)

    # Home Locator
    btn_home_path = (
        By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/home_page/target/home_btn.png",
        browser_image_path)

    btn_home = ImageWebdriverPageElement(btn_home_path)

    # Home Locator
    btn_projects_path = (
        By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/home_page/target/projects_btn.png",
        browser_image_path)

    btn_projects = ImageWebdriverPageElement(btn_projects_path)
