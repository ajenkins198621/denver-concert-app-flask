#!/usr/bin/env python3
"""
Basic entry into the Denver Concerts web application
"""
from datetime import datetime, timedelta
from flask import request, render_template, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from sqlalchemy.orm import joinedload

from applications.create_app import create_app
from db.models import Concert, ConcertArtist

app = create_app()

HOMEPAGE_RESULTS = Counter(
    'homepage_requests', 'Number of requests made to the homepage')
HEALTH_CHECK_RESULTS = Counter(
    'health_check_requests', 'Number of requests made to the health check')
GET_CONCERTS_RESULTS = Counter(
    'get_concerts_requests', 'Number of requests made to get concerts')


@app.route("/")
def main() -> str:
    '''
    Route: Web Application Homepage
    '''
    data = {
        "title": "Denver Rock Concerts",
        # "content": form
    }
    HOMEPAGE_RESULTS.inc()
    return render_template('index.html', data=data)


@app.route("/health-check")
def health_check() -> str:
    '''
    Route: Health Check
    '''
    HEALTH_CHECK_RESULTS.inc()
    return "I'm Healthy!"


@app.route("/get-concerts", methods=["GET"])
def get_concerts_json():
    '''
    Gets the JSON response of all concerts
    '''
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        return jsonify({"error": "Please enter a valid page number."}), 400

    if page < 1:
        return jsonify({"error": "Page number must be 1 or greater."}), 400

    current_date = datetime.utcnow()
    start_date = current_date + timedelta(days=(page - 1) * 30)
    end_date = start_date + timedelta(days=30)

    concerts = Concert.query.filter(
        Concert.date >= start_date,
        Concert.date < end_date
    ).options(
        joinedload(Concert.concert_artists).joinedload(ConcertArtist.artist)
    ).order_by(Concert.date).all()

    concerts_data = [concert.concert_to_dict(include_artists=True, include_venue=True)
                     for concert in concerts]
    grouped_concerts = group_concerts(concerts_data)
    GET_CONCERTS_RESULTS.inc()
    return jsonify(grouped_concerts)


@app.route('/metrics')
def metrics():
    return generate_latest(), {'Content-Type': CONTENT_TYPE_LATEST}


def group_concerts(concerts) -> dict:
    '''
    Helper function that groups the concerts by date
    '''
    dates = {}
    for concert in concerts:
        concert['formatted_date'] = concert['date'].strftime('%Y-%m-%d')
        if concert['formatted_date'] not in dates:
            dates[concert['formatted_date']] = {
                'dateLabel': concert['date'].strftime('%A, %B %d, %Y'),
                'concerts': []
            }
        dates[concert['formatted_date']]['concerts'].append(concert)
    return dates


if __name__ == '__main__':
    app.run()
