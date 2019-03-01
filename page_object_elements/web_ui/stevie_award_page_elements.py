from selenium.webdriver.common.by import By
from lib.page_objects import PageElement


class StevieAwardPageElements:
    # Defining locators and webelements.
    btn_vote_for_belatrix_loc = (By.XPATH, "//div[@class='gallery_col clearfix']/div[@class='gallery_desc ']//a[contains(.,'belatrix')]/parent::p/preceding-sibling::h3/a")
    btn_vote_for_belatrix = PageElement(btn_vote_for_belatrix_loc)

    lbl_nominated_company_loc = (By.XPATH, "//div[@class='voteConfirmation']/div[1]")
    lbl_nominated_company = PageElement(lbl_nominated_company_loc)

    lbl_confirm_your_selection_loc = (By.XPATH, "//*[@id='templateBody']//p")
    lbl_confirm_your_selection = PageElement(lbl_confirm_your_selection_loc)

    btn_confirm_vote_loc = (By.XPATH, "//input[@class='confirmVote button']")
    btn_confirm_vote = PageElement(btn_confirm_vote_loc)

    lbl_voting_confirmation_loc = (By.XPATH, "//div[@class='voteComplete']/div[1]/p")
    lbl_voting_confirmation = PageElement(lbl_voting_confirmation_loc)

    btn_cancel_and_go_back_loc = (By.XPATH, "//input[@class='back button']")
    btn_cancel_and_go_back = PageElement(btn_cancel_and_go_back_loc)