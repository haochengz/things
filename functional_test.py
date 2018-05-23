
"""
This Module include the TestCase of the website
"""

import unittest
from selenium import webdriver

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
