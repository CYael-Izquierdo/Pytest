from selenium.webdriver.common.by import By
from lib.page_objects import PageElement, MultiPageElement


class IosGooglePageElement:

    txt_search_loc = (By.XPATH, '//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
    txt_search = PageElement(txt_search_loc)

    btn_search_loc = (By.XPATH, '//div[@class="zGVn2e"]//button[@class="Tg7LZd"]')
    btn_search = PageElement(btn_search_loc)

    result_titles_list_loc = (By.XPATH, '//*[@id="rso"]//div[@class="MUxGbd v0nnCb"]')
    '//*[@id="arc-srp_1920-0"]/div/div[3]/div[2]/div/div[1]/a/div[1]'
    result_titles_list = MultiPageElement(result_titles_list_loc)

    btn_more_results_loc = (By.XPATH, '//*[@id="botstuff"]//span[@class="RVQdVd"]')
    btn_more_results = PageElement(btn_more_results_loc)
