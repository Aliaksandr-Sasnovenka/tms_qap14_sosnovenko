from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service

"""Contains code for common issues of the POM"""


class BasePage:
    # Made on the basis of hw20life.py
    def __init__(self):
        # self.service = Service(driver)
        self.browser = webdriver.Edge()

    def click(self, by_locator):
        # click on page element through locators_PAc.py
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def text_is(self, by_locator, text):
        # Returns any text of items of interest
        WebDriverWait(self.browser, 20).until(EC.text_to_be_present_in_element(by_locator, text))

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        tit = WebDriverWait(self.browser, 20).until(EC.title_is(title))
        return tit  # true or false

    def get_frame(self, by_locator):
        # switch to the desired frame
        WebDriverWait(self.browser, 20).until(EC.frame_to_be_available_and_switch_to_it(by_locator))

    def get_list_of_elements(self, by_locator):
        # top_element = self.browser.find_element(self, by_locator)
        list_cont = self.browser.find_elements(by_locator)
        return list_cont

    def get_back_from_iframe(self):
        self.browser.switch_to.default_content()

    def get_alert_text(self):
        alert_message = []
        is_present = WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        if is_present:
            alert = self.browser.switch_to.alert
            alert_message = alert.text
        return alert_message
