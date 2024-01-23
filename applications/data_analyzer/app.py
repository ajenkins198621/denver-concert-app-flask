#!/usr/bin/env python3
'''
Analyzes and stores data from the Ticketmaster Discovery API
'''

import logging
from datetime import datetime
from applications.create_app import create_app
from db.db import db
from db.models import ConcertRaw, Artist, Venue, Concert, ConcertArtist

app = create_app()


def store_concerts_from_raw_data() -> str:
    '''
    Entry point for storing concerts from raw data
    '''

    num_concerts_inserted = 0

    raw_results = ConcertRaw.query.all()

    for raw_result in raw_results:
        result = raw_result.decode_raw()
        if result is not None:
            if "_embedded" in result:
                if "events" in result["_embedded"]:
                    concerts = result["_embedded"]["events"]
                    for concert in concerts:
                        num_concerts_inserted += store_concert(concert)
        else:
            pass

        db.session.delete(raw_result)

    db.session.commit()
    logging.info(f"Stored %s concerts", num_concerts_inserted)
    return f"Stored {num_concerts_inserted} concerts"


def store_concert(concert: dict) -> int:
    '''
    Stores the concerts in the database
    '''

    concert_ticketmaster_id = concert['id']
    concert_name = concert['name']
    concert_image_url = None
    concert_date = ""
    concert_venue_id = -1
    artist_ids = []

    # Check if existing Concert by Ticketmaster ID
    existing_concert = Concert.query.filter_by(
        ticketmaster_id=concert_ticketmaster_id).first()
    if existing_concert and existing_concert.id:
        print(
            f"Concert: Duplicate concert: {concert_ticketmaster_id}, {concert_name}")
        return 0

    # Create Artists
    if "_embedded" in concert:
        embedded = concert["_embedded"]
        if "attractions" in embedded and len(embedded["attractions"]) > 0:
            concert_artists = embedded["attractions"]
            for artist in concert_artists:
                artist_id = store_artist(artist)
                if (artist_id != 0):
                    artist_ids.append(artist_id)
                    print("ARTIST ID: ", artist_id)

        # Create Venues if they don't exist
        if "venues" in embedded:
            for venue in embedded["venues"]:
                venue_id = store_venue(venue)
                if (venue_id != 0):
                    concert_venue_id = venue_id
                    print("VENUE ID: ", concert_venue_id)

    # Create Concert
    if "images" in concert and len(concert["images"]) > 0:

        concert_image_url = ""

        for image in concert["images"]:
            if image["height"] > 150 and image["height"] < 350 and image["ratio"] == "4_3":
                concert_image_url = image['url']
                break
        if concert_image_url == "":
            for image in concert["images"]:
                if image["height"] > 150 and image["height"] < 350 and image["ratio"] == "3_2":
                    concert_image_url = image['url']
                    break
        if concert_image_url == "":
            concert_image_url = concert['images'][0]['url']

    if "dates" in concert:
        if "start" in concert["dates"]:
            if "localDate" in concert["dates"]["start"]:
                concert_date = concert["dates"]["start"]["localDate"]

    new_concert = Concert(
        ticketmaster_id=concert_ticketmaster_id,
        name=concert_name,
        image_url=concert_image_url,
        date=datetime.strptime(concert_date, '%Y-%m-%d'),
        venue_id=concert_venue_id
    )
    db.session.add(new_concert)
    db.session.commit()

    # Create ConcertArtists
    for artist_id in artist_ids:
        new_concert_artist = ConcertArtist(
            concert_id=new_concert.id,
            artist_id=artist_id
        )
        db.session.add(new_concert_artist)

    db.session.commit()
    return 1


def store_artist(artist: dict) -> int:
    '''
    Stores the artists in the database
    '''

    artist_ticketmaster_id = artist['id']
    artist_name = artist['name']
    artist_spotify_url = None
    artist_image_url = None

    # Check if existing Artist by Ticketmaster ID

    if not artist_ticketmaster_id:
        print("Artist: No Ticketmaster ID")
        return 0

    existing_artist = Artist.query.filter_by(
        ticketmaster_id=artist_ticketmaster_id).first()
    if existing_artist and existing_artist.id:
        print(
            f"Artist: Duplicate artist: {artist_ticketmaster_id}, {artist_name}")
        return 0

    if "externalLinks" in artist:
        if "spotify" in artist["externalLinks"] and len(artist["externalLinks"]['spotify']) > 0:
            artist_spotify_url = artist["externalLinks"]['spotify'][0]['url']
    if "images" in artist and len(artist["images"]) > 0:
        artist_image_url = artist['images'][0]['url']

    new_artist = Artist(
        ticketmaster_id=artist_ticketmaster_id,
        name=artist_name,
        spotify_url=artist_spotify_url,
        image_url=artist_image_url
    )

    db.session.add(new_artist)
    db.session.commit()

    return new_artist.id


def store_venue(venue: dict) -> int:
    '''
    Stores the venue in the database
    '''

    venue_ticketmaster_id = venue['id']
    venue_name = venue['name']
    venue_address_1 = ""
    venue_address_2 = ""
    if "address" in venue:
        if "line1" in venue['address']:
            venue_address_1 = venue['address']['line1']
        if "line2" in venue['address']:
            venue_address_2 = venue['address']['line2']
    venue_city = ""
    if "city" in venue:
        if "name" in venue['city']:
            venue_city = venue['city']['name']
    venue_state = ""
    if "state" in venue:
        if "stateCode" in venue['state']:
            venue_state = venue['state']['stateCode']
    venue_zip = venue['postalCode']
    venue_image_url = None
    if "images" in venue and len(venue["images"]) > 0:
        venue_image_url = venue['images'][0]['url']

    if not venue_ticketmaster_id:
        print("Venue: No Ticketmaster ID")
        return 0

    existing_venue = Venue.query.filter_by(
        ticketmaster_id=venue_ticketmaster_id).first()
    if existing_venue and existing_venue.id:
        print(f"Venue: Duplicate venue: {venue_ticketmaster_id}, {venue_name}")
        return existing_venue.id

    new_venue = Venue(
        ticketmaster_id=venue_ticketmaster_id,
        name=venue_name,
        address1=venue_address_1,
        address2=venue_address_2,
        city=venue_city,
        state=venue_state,
        zipcode=venue_zip,
        image_url=venue_image_url
    )

    db.session.add(new_venue)
    db.session.commit()
    return new_venue.id


if __name__ == "__main__":
    # Use app context for database operations
    with app.app_context():
        store_concerts_from_raw_data()
