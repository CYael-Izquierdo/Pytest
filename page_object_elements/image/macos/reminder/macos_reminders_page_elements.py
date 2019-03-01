from appium.webdriver.common.mobileby import MobileBy as By
from lib.page_objects import ImageDesktopPageElement
from lib import util


class MacOsRemindersPagePageElements:
    __project_root_path = util.get_proyect_root_path()
    desktop_image_path = __project_root_path + "/reports/visual_image_testing/MacOsRemindersPage.png"
    reminder_standard_image_path = __project_root_path + "/page_object_elements/image/macos/reminder/standard/reminders_main_standard.png"
    default_threshold = 0.99

    # Reminder Name prompt
    txt_reminder_name_prompt_loc = __project_root_path + \
                                   "/page_object_elements/image/macos/reminder/target/txt_reminders_prompt.png"
    txt_reminder_name_prompt = ImageDesktopPageElement(locator=txt_reminder_name_prompt_loc,
                                                       desktop_image_path=desktop_image_path,
                                                       threshold=0.95)
    # Reminder Name
    txt_reminder_name_loc = __project_root_path + \
                            "/page_object_elements/image/macos/reminder/target/txt_reminder_name.png"
    txt_reminder_name = ImageDesktopPageElement(locator=txt_reminder_name_loc,
                                                desktop_image_path=desktop_image_path,
                                                threshold=0.90)

    # Add Reminder button
    btn_add_reminder_method = "TM_CCOEFF_NORMED"
    btn_add_reminder_loc = __project_root_path + \
                           "/page_object_elements/image/macos/reminder/target/btn_add_reminder.png"

    btn_add_reminder = ImageDesktopPageElement(locator=btn_add_reminder_loc,
                                               desktop_image_path=desktop_image_path,
                                               method=btn_add_reminder_method,
                                               threshold=0.99)
    # File Menu
    menu_file_loc = __project_root_path + \
                    "/page_object_elements/image/macos/reminder/target/menu_file.png"
    menu_file = ImageDesktopPageElement(locator=menu_file_loc,
                                        desktop_image_path=desktop_image_path,
                                        threshold=0.90)

    # File >> New Reminder
    menu_file_new_reminder_loc = __project_root_path + \
                                 "/page_object_elements/image/macos/reminder/target/menu_file_new_reminder.png"
    menu_file_new_reminder = ImageDesktopPageElement(locator=menu_file_new_reminder_loc,
                                                     desktop_image_path=desktop_image_path,
                                                     threshold=0.90)
    # Button info
    btn_info_loc = __project_root_path + \
                   "/page_object_elements/image/macos/reminder/target/btn_info.png"
    btn_info_method = "TM_CCOEFF"
    btn_info = ImageDesktopPageElement(locator=btn_info_loc,
                                       desktop_image_path=desktop_image_path,
                                       threshold=0.80)

    # Context Menu - Show info
    context_menu_show_info_loc = __project_root_path + \
                                 "/page_object_elements/image/macos/reminder/target/context_menu_show_info.png"
    context_menu_show_info = ImageDesktopPageElement(locator=context_menu_show_info_loc,
                                                     desktop_image_path=desktop_image_path,
                                                     threshold=0.80)
    # On a day
    chk_on_a_day_loc = __project_root_path + \
                       "/page_object_elements/image/macos/reminder/target/chk_on_a_day.png"
    chk_on_a_day = ImageDesktopPageElement(locator=chk_on_a_day_loc,
                                           desktop_image_path=desktop_image_path,
                                           threshold=0.85)

    # Priority
    sel_priority_loc = __project_root_path + \
                       "/page_object_elements/image/macos/reminder/target/sel_priority.png"
    sel_priority = ImageDesktopPageElement(locator=sel_priority_loc,
                                           desktop_image_path=desktop_image_path,
                                           threshold=0.90)

    # Priority Low
    sel_priority_low_loc = __project_root_path + \
                           "/page_object_elements/image/macos/reminder/target/sel_priority_low.png"

    sel_priority_low = ImageDesktopPageElement(locator=sel_priority_low_loc,
                                               desktop_image_path=desktop_image_path,
                                               threshold=0.90)

    # Priority Medium
    sel_priority_medium_loc = __project_root_path + \
                              "/page_object_elements/image/macos/reminder/target/sel_priority_medium.png"
    sel_priority_medium = ImageDesktopPageElement(locator=sel_priority_medium_loc,
                                                  desktop_image_path=desktop_image_path,
                                                  threshold=0.90)

    # Priority high
    sel_priority_high_loc = __project_root_path + \
                            "/page_object_elements/image/macos/reminder/target/sel_priority_high.png"
    sel_priority_high = ImageDesktopPageElement(locator=sel_priority_high_loc,
                                                desktop_image_path=desktop_image_path,
                                                threshold=0.90)
    # Notes
    txt_note_loc = __project_root_path + \
                   "/page_object_elements/image/macos/reminder/target/txt_note.png"
    txt_note = ImageDesktopPageElement(locator=txt_note_loc,
                                       desktop_image_path=desktop_image_path,
                                       threshold=0.95)

    # Done
    btn_done_loc = __project_root_path + \
                   "/page_object_elements/image/macos/reminder/target/btn_done.png"
    btn_done = ImageDesktopPageElement(locator=btn_done_loc,
                                       desktop_image_path=desktop_image_path,
                                       threshold=0.90)

    # View Menu
    menu_view_loc = __project_root_path + \
                   "/page_object_elements/image/macos/reminder/target/menu_view.png"
    menu_view = ImageDesktopPageElement(locator=menu_view_loc,
                                       desktop_image_path=desktop_image_path,
                                       threshold=0.90)

    # View Menu >> Enter Full screen
    menu_view_enter_full_screen_loc = __project_root_path + \
                   "/page_object_elements/image/macos/reminder/target/menu_view_enter_full_screen.png"
    menu_view_enter_full_screen = ImageDesktopPageElement(locator=menu_view_enter_full_screen_loc,
                                       desktop_image_path=desktop_image_path,
                                       threshold=0.90)

    # Send lbl_send_the_weekly_report
    lbl_send_the_weekly_report_loc = __project_root_path + \
                                      "/page_object_elements/image/macos/reminder/target/lbl_send_the_weekly_report.png"
    lbl_send_the_weekly_report = ImageDesktopPageElement(locator=lbl_send_the_weekly_report_loc,
                                                          desktop_image_path=desktop_image_path,
                                                          threshold=0.85)

    # Send lbl_send_the_weekly_report
    context_menu_delete_loc = __project_root_path + \
                                     "/page_object_elements/image/macos/reminder/target/context_menu_delete.png"
    context_menu_delete = ImageDesktopPageElement(locator=context_menu_delete_loc,
                                                         desktop_image_path=desktop_image_path,
                                                         threshold=0.95)