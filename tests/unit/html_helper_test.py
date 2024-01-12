"""
Unit tests for the htmlhelper.py web application
"""
import unittest
from applications.web.htmlhelper import HtmlHelper


class TestHtmlHelper(unittest.TestCase):
    """
    Test the HTML Helper functions
    """

    def setUp(self):
        """
        Instantiate the HtmlHelper class
        """
        self.htmlHelper = HtmlHelper()

    def test_gets_header(self):
        """
        Tests the get_header() function
        """

        title = "This is a unit test!"
        header_content = self.htmlHelper.get_header(title=title)
        self.assertIsInstance(header_content, str)
        self.assertIn(title, header_content)

    def test_gets_footer(self):
        """
        Tests the get_footer() function
        """

        footer_content = self.htmlHelper.get_footer()
        self.assertIsInstance(footer_content, str)


if __name__ == '__main__':
    unittest.main()
