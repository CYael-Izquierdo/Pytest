from page_objects.image.image_desktop_page import ImageDesktopPage
from page_object_elements.image.macos.macos_desktop_page_elements import MacOsDesktopPagePageElements
from page_object_elements.image.macos.macos_launchpad_page_elements import MacOsLaunchpadPagePageElements
from retry.api import retry


class MacOsDesktopPage(ImageDesktopPage, MacOsDesktopPagePageElements):

    def __init__(self):
        super(MacOsDesktopPage, self).__init__(class_name=MacOsDesktopPage.__name__)

    def click_on_menu_bar_icon(self, icon_name):
        if icon_name.lower() == "launchpad":
            self.icon_launchpad.click()


class MacOsLaunchpadPage(ImageDesktopPage, MacOsLaunchpadPagePageElements):

    def __init__(self):
        super(MacOsLaunchpadPage, self).__init__(class_name=MacOsLaunchpadPage.__name__)

    @retry(exceptions=Exception, tries=5, delay=0.1)
    def open_application(self, app_name):
        if app_name.lower() == "reminders":
            self.icon_reminders.click()

    # TODO: Fix why does not do click on search_app
    def search_app(self, app_name):
        raise Exception("search_app method needs to be fixed.")
        self.txt_search_app.click()
        self.txt_search_app = app_name

    def search_and_open_app(self, app_name):
        self.search_app(app_name=app_name)
        self.open_application(app_name=app_name)
