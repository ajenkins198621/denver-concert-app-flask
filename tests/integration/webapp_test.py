"""
Import the main entry to my web application
"""

import unittest
from applications.web.app import app


class WebAppIntegrationTest(unittest.TestCase):
    """
    Tests the web application
    """

    def setUp(self):
        """
        Initial Setup
        """
        app.config.update({
            "TESTING": True,
        })
        self.client = app.test_client()

    def test_homepage_route(self):
        """
        Tests the homepage route
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Loading concerts...", response.data.decode())


if __name__ == '__main__':
    unittest.main()
