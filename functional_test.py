
"""
This Module include the TestCase of the website
"""

import unittest
from selenium import webdriver


class FunctionalTest(unittest.TestCase):
    """
    Functional Test
    """

    def setUp(self):
        self.browser = create_browser()

    def tearDown(self):
        self.browser.quit()

    def test_server_started(self):
        """
        Test Server was started
        """
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn('Django', self.browser.title)

    def reset_browser(self):
        """
        Create a new headless browser and close the one before
        """
        self.browser.quit()
        self.browser = create_browser()


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
