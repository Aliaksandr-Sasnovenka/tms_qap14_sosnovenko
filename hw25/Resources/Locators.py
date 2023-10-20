from selenium.webdriver.common.by import By


class ElementsLocator:
    iframe_tag = (By.ID, "mce_0_ifr")
    iframe_body = (By.TAG_NAME, "body")
    iframe_button = (By.CLASS_NAME, "tox-mbtn__select-label")
    get_element_by_CSS_attr = (By.CSS_SELECTOR, "button[title=Bold]")
    ll_of_elements = (By.XPATH, "//body//*")
