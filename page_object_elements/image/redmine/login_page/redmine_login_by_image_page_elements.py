from appium.webdriver.common.mobileby import MobileBy as By
from lib.page_objects import ImageWebdriverPageElement
from lib import util


class RedmineLoginByImagePagePageElements:
    __project_root_path = util.get_proyect_root_path()
    browser_image_path = __project_root_path + "/reports/visual_image_testing/RedmineLoginByImagePage_SCREENSHOT.png"
    threshold = 0.99

    # Home Standard Image
    login_page_standard_path = (By.IMAGE, __project_root_path +
                                "/page_object_elements/image/redmine/login_page/standard/login_page.png",
                                browser_image_path)
    login_page_standard = ImageWebdriverPageElement(login_page_standard_path)

    # Login Locator
    txt_login_in_path = (By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/login_page/target/txt_login.png",
                         browser_image_path)

    txt_login_in = ImageWebdriverPageElement(txt_login_in_path, threshold=0.74)

    # Password Locator
    txt_password_path = (By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/login_page/target/txt_password.png",
                         browser_image_path)

    txt_password = ImageWebdriverPageElement(txt_password_path, threshold=threshold)

    # Login button Locator
    btn_login_path = (By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/login_page/target/btn_login.png",
                      browser_image_path)

    btn_login = ImageWebdriverPageElement(btn_login_path, threshold=threshold)

    # Lost Password Locator
    btn_lost_password_path = (By.IMAGE, __project_root_path + "/page_object_elements/image/redmine/login_page/target/bnt_lost_password.png",
                              browser_image_path)

    btn_lost_password = ImageWebdriverPageElement(btn_lost_password_path, threshold=threshold)
