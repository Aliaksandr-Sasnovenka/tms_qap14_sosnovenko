from hw25.Pages.base_page import BasePage
from hw25.Resources.Locators import ElementsLocator
from selenium.webdriver.common.by import By
from random import randrange


class HerokuappPage(BasePage):

    def __init__(self):
        super().__init__()
        self.browser.get('https://the-internet.herokuapp.com/iframe')

    def number_of_element(self):
        # return a relative row position of one of the siblings element
        number = 0
        number_of_iframes_field_elements = len(self.browser.find_elements(By.XPATH, "//body//*"))
        try:
            number = randrange(0, number_of_iframes_field_elements, 1)
        except:
            print("Too low list's elements")
        if number_of_iframes_field_elements == 1:
            number = 1
        return number

    def click_on_any_elementof_iframes_textfield(self, number):
        # Function must get one of the siblings of the top elements
        child_element = (By.XPATH, f"(//body)[{number}]")
        self.click(child_element)
        return child_element

    def get_next_element(self, number):
        # next_element = (By.XPATH, f"(//body)[{number}]")
        next_el = self.browser.find_element(By.XPATH, f"(//body)[{number}]")
        return next_el

    def click_bold_button(self):
        self.click(ElementsLocator.get_element_by_CSS_attr)
