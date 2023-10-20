import unittest
from hw25.Pages.herokuapp_page import HerokuappPage
from hw25.Resources.Locators import ElementsLocator


class TestHw25(unittest.TestCase):
    def setUp(self):
        self.page = HerokuappPage()

    def test_fonts_bold_action(self):
        """It is going to be necessary to access the possibility of a bold action over the text that was selected in
        the text field of an iframe previously"""
        self.page.get_frame(ElementsLocator.iframe_tag)  # jump on the iframe
        number = self.page.number_of_element()  # take a random number of iframe's textfield
        element = self.page.click_on_any_elementof_iframes_textfield(number)
        self.page.get_back_from_iframe()  # take a choice and get back to the default page
        self.page.click_bold_button()  # try to do the place where we clicked with bold view and strong tag
        self.page.get_frame(ElementsLocator.iframe_tag)
        new_element = self.page.get_next_element(
            number + 1)  # it's expected that new element was included after the B-button was clicked
        print(new_element.tag_name)
        self.assertEqual(new_element.tag_name, "span", "Stronglessness")

    def tearDown(self):
        # close the browser window
        self.page.browser.close()

    if __name__ == "__main__":
        unittest.main()
