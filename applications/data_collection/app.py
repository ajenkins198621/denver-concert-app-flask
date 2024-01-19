#!/usr/bin/env python3
'''
Gets concert data from the API and stores it in the database
'''

from datetime import datetime, timedelta
import json
import os
import requests

from applications.create_app import create_app
from db.db import db
from db.models import ConcertRaw

app = create_app()

base_api_url = "https://app.ticketmaster.com/discovery/v2/events.json"


def get_concerts_around_denver(current_month: int = 0, override_url: str = "") -> dict:
    '''
    Gets concerts from Ticketmaster Discovery API
    '''

    # Current date and end of the current month
    start_date = datetime.now() + timedelta(days=31 * current_month)
    end_date = start_date + timedelta(days=31)

    params = {
        "apikey": os.environ["TICKETMASTER_DISCOVERY_API_KEY"],
        # "keyword": "concert",
        "radius": "25",
        "unit": "miles",
        "geoPoint": "39.7392,-104.9903",  # GeoPoint for Denver
        "segmentId": "KZFzniwnSyZfZ7v7nJ",  # Music
        "genreId": [
            "KnvZfZ7vAeA",  # Rock
            "KnvZfZ7vAvv",  # Alternative
            "KnvZfZ7vAvt",  # Metal
            "KnvZfZ7vAed"  # Reggae
        ],
        "size": 200,  # Max # of results, this is the max allowed by Ticketmaster API
        "startDateTime": start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "endDateTime": end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    if override_url:
        response = requests.get(override_url, timeout=30)
    else:
        response = requests.get(base_api_url, params=params, timeout=30)
    return response.json()


def get_concerts() -> str:
    '''
    Gets 12 months of concerts and stores the raw data in the database
    '''

    concert_count = 0

    # Get concerts for the next 12 months
    for i in range(12):
        concerts = get_concerts_around_denver(current_month=i)

        if "page" in concerts:
            if "totalElements" in concerts["page"]:
                concert_count += concerts["page"]["totalElements"]
            else:
                continue

        insert_raw_concert_data(concerts)

        # Loop through subsequent pages if applicable
        is_complete = False
        while not is_complete:
            if "_links" in concerts:
                if "next" not in concerts["_links"]:
                    is_complete = True
                    break
                else:
                    next_url = concerts["_links"]["next"]["href"]
                    concerts = get_concerts_around_denver(
                        current_month=i, override_url=next_url)
                    insert_raw_concert_data(concerts)

    return f"Imported {concert_count} concerts' raw data"


def insert_raw_concert_data(json_dict: dict) -> bool:
    '''
    Inserts raw concert data into the database
    '''
    try:
        json_string = json.dumps(json_dict)
        new_concert_raw = ConcertRaw(raw=json_string)
        db.session.add(new_concert_raw)
        db.session.commit()
    except Exception as e:
        print(e)
        return False
    return True


if __name__ == "__main__":
    # Use app context for database operations
    with app.app_context():
        get_concerts()
