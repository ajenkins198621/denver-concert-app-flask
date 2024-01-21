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
        self.assertIn("How are you feeling today?", response.data.decode())

    def test_display_info_route_shows_nothing(self):
        """
        Tests the route which displays information when no data is provided
        """
        response = self.client.post(
            "/display-user-input", data={'user_feeling': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Nothing", response.data.decode())

    def test_display_info_route_shows_message(self):
        """
        Tests the route which displays information when no data is provided
        """
        user_feeling = "I feel great, thanks!"
        response = self.client.post(
            "/display-user-input", data={'user_feeling': user_feeling})
        self.assertEqual(response.status_code, 200)
        self.assertIn(user_feeling, response.data.decode())


if __name__ == '__main__':
    unittest.main()
