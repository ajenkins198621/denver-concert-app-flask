'''
Integration tests for data collection app
'''
import json
import unittest
from unittest.mock import patch

from applications.data_collection.app import app, db, get_concerts_around_denver
from db.models import ConcertRaw


test_response = {
    "_embedded": {
        "events": [
            {
                "name": "Test Event 1",
            },
            {
                "name": "Test Event 2",
            }
        ]
    },
    "page": {
        "totalElements": 2
    }
}


class DataCollectionTest(unittest.TestCase):
    '''
    Tests the data collection application
    '''

    def setUp(self):
        app.config.update({
            "SQLALCHEMY_DATABASE_URI": 'sqlite:///:memory:',
            "TESTING": True
        })
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_concerts_around_denver(self):
        '''
        Test getting data from the API
        '''
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = test_response
            concerts = get_concerts_around_denver()
            self.assertEqual(concerts["_embedded"]["events"][0]["name"],
                             "Test Event 1")
            self.assertEqual(concerts["_embedded"]["events"][1]["name"],
                             "Test Event 2")
            self.assertEqual(concerts["page"]["totalElements"], 2)

    def test_insert_raw_concert_data(self):
        '''
        Test inserting raw concert data
        '''
        concert = ConcertRaw(
            raw=json.dumps(test_response)
        )
        db.session.add(concert)
        db.session.commit()
        self.assertEqual(ConcertRaw.query.count(), 1)
        self.assertEqual(ConcertRaw.query.first().raw,
                         json.dumps(test_response))
