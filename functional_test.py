
"""
This Module include the TestCase of the website
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from vars import addr


class FunctionalTest(unittest.TestCase):
    """
    Functional Test
    """

    def setUp(self):
        self.browser = create_browser()

    def tearDown(self):
        self.browser.quit()

    def reset_browser(self):
        """
        Create a new headless browser and close the one before
        """
        self.browser.quit()
        self.browser = create_browser()

    def test_server_renders_index_page(self):
        """
        Test Server was started
        """
        self.browser.get(addr)
        self.assertIn('To-do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-do", header_text)

        inputbox = self.browser.find_element_by_id("new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)

        self.browser.get(addr)
        table = self.browser.find_element_by_id("list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )


def create_browser():
    """
    Create a new headless browser
    """
    ff_options = webdriver.FirefoxOptions()
    ff_options.set_headless()
    browser = webdriver.Firefox(options=ff_options)
    browser.implicitly_wait(3)
    return browser


if __name__ == "__main__":
    unittest.main()
