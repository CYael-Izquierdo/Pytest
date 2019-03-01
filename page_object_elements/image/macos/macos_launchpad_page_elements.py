from appium.webdriver.common.mobileby import MobileBy as By
from lib.page_objects import ImageDesktopPageElement
from lib import util


class MacOsLaunchpadPagePageElements:
    __project_root_path = util.get_proyect_root_path()
    desktop_image_path = __project_root_path + "/reports/visual_image_testing/MacOsDesktopPage.png"
    default_threshold = 0.99

    # Search App Locator
    txt_search_app_loc = __project_root_path + "/page_object_elements/image/macos/desktop/target/txt_search_app.png"
    txt_search_app = ImageDesktopPageElement(locator=txt_search_app_loc,
                                             desktop_image_path=desktop_image_path,
                                             threshold=default_threshold)

    # Search App Locator
    icon_reminders_loc = __project_root_path + "/page_object_elements/image/macos/desktop/target/icon_reminders.png"
    icon_reminders = ImageDesktopPageElement(locator=icon_reminders_loc,
                                             desktop_image_path=desktop_image_path,
                                             threshold=0.80)
