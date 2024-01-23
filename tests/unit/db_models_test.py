'''
Unit tests for database models
'''
from datetime import datetime, timedelta
import unittest
from applications.create_app import create_app, db
from db.models import ConcertRaw, ConcertArtist, Concert, Artist, Venue


class TestDatabaseModels(unittest.TestCase):
    '''
    Tests the data collection application
    '''

    def setUp(self):
        app = create_app(config_name='testing')
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

    def test_concert_to_dict(self):
        venue = Venue(name="Red Rocks", address1="123 Street", city="Denver")
        artist = Artist(name="Band A", spotify_url="spotify.com/123")
        concert = Concert(name="Concert 1", venue=venue)
        concert_artists = ConcertArtist(concert=concert, artist=artist)

        concert.concert_artists = [concert_artists]
        concert.venue = venue

        concert_dict = concert.concert_to_dict(
            include_artists=True, include_venue=True)
        self.assertEqual(concert_dict['name'], concert.name)
        self.assertEqual(concert_dict['artists'][0]['name'], artist.name)
        self.assertEqual(concert_dict['venue']['name'], venue.name)

    def test_decode_raw_valid_json(self):
        '''
        Tests the decode_raw method
        '''
        concert_raw = ConcertRaw(raw='{"key": "value"}')
        decoded = concert_raw.decode_raw()
        self.assertEqual(decoded, {"key": "value"})

    def test_decode_raw_invalid_json(self):
        '''
        Tests the decode_raw method
        '''
        concert_raw = ConcertRaw(raw='invalid json')
        decoded = concert_raw.decode_raw()
        self.assertIsNone(decoded)

    def test_artist_to_dict(self):
        artist = Artist(ticketmaster_id="abc123", name="ABC",
                        spotify_url="http://def.com")
        artist_dict = artist.artist_to_dict()
        self.assertEqual(artist_dict['name'], artist.name)
        self.assertEqual(artist_dict['spotify_url'], artist.spotify_url)

    def test_model_relationships(self):
        venue = Venue(ticketmaster_id="abc123", name="Bluebird Theater")
        artist = Artist(ticketmaster_id="abc123", name="asdsfasdf")
        concert = Concert(ticketmaster_id="abc123",
                          name="dssagasd", venue=venue, image_url="http://asdf.com", date=datetime.now() + timedelta(days=31 * 1))
        concert_artist = ConcertArtist(concert=concert, artist=artist)

        # Adding to DB session for relationship testing
        db.session.add(venue)
        db.session.add(artist)
        db.session.add(concert)
        db.session.add(concert_artist)
        db.session.commit()

        self.assertIn(concert_artist, concert.concert_artists)
        self.assertIn(concert_artist, artist.artist_concerts)


if __name__ == '__main__':
    unittest.main()
