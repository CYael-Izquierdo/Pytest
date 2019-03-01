from page_objects.web_ui.webui_base_page import WebuiBasePage
from page_object_elements.web_ui.stevie_award_page_elements import StevieAwardPageElements


class StevieAwardPage(WebuiBasePage, StevieAwardPageElements):

    def __init__(self, driver):
        super(StevieAwardPage, self).__init__(driver)

    def vote(self):
        self.wait_for_element_to_be_clickable(element_locator=self.btn_vote_for_belatrix_loc, waiting_time=10)
        self.scroll_to(web_element=self.btn_vote_for_belatrix)
        self.btn_vote_for_belatrix.click()

    def get_confirmation_message(self):
        return self.lbl_confirm_your_selection.text

    def get_confirmation_nominated_company(self):
        return self.lbl_nominated_company.text

    def get_voting_confirmation(self):
        return self.lbl_voting_confirmation.text

    def confirm_vote(self):
        self.btn_confirm_vote.click()

