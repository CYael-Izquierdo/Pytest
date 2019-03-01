from appium.webdriver.common.mobileby import MobileBy as By
from lib.page_objects import ImageDesktopPageElement
from lib import util


class MacOsDesktopPagePageElements:
    __project_root_path = util.get_proyect_root_path()
    desktop_image_path = __project_root_path + "/reports/visual_image_testing/MacOsDesktopPage.png"
    threshold = 0.99

    # Login Locator
    icon_launchpad_path = __project_root_path + "/page_object_elements/image/macos/desktop/target/icon_launchpad.png"
    icon_launchpad = ImageDesktopPageElement(locator=icon_launchpad_path,
                                             desktop_image_path=desktop_image_path,
                                             threshold=0.95)

