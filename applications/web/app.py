#!/usr/bin/env python3
"""
Basic entry into the Denver Concerts web application
"""
from datetime import datetime, timedelta
from flask import request, render_template, jsonify
from sqlalchemy.orm import joinedload

from applications.create_app import create_app
from db.models import Concert, ConcertArtist

app = create_app('applications/web/templates')


@app.route("/")
def main() -> str:
    '''
    Route: Web Application Homepage
    '''
    # form = '''
    # <form action="/display-user-input" method="POST" style="display: flex; flex-direction: column; margin-block-end: 0;">
    #     <label for="user_feeling" style="font-size: 24px; margin-bottom: 16px; font-family: sans-serif;">👋 How are you feeling today?</label>
    #     <input type="text" name="user_feeling" id="user_feeling" placeholder="Good, bad, ready to rock, etc..." style="height: 36px; border-radius 40px; padding: 10px 20px; font-size: 24px;" />
    #     <input type="submit" value="✉️ SUBMIT" style="background: #080808; color: #fff; margin-top: 16px; height: 36px; border-radius: 40px; text-align: center; font-size: 24px; border: none;" />
    #  </form>
    # '''
    data = {
        "title": "Denver Rock Concerts",
        # "content": form
    }
    return render_template('index.html', data=data)


@app.route("/display-user-input", methods=["POST"])
def echo_unput() -> str:
    '''
    Route: After User Input
    '''
    input_text = request.form.get("user_feeling", "")
    if not input_text:
        input_text = "Nothing 😢"
    content = f'''
        <p style="font-size: 18px; margin-bottom: 16px; font-family: sans-serif; text-align: center; color: #666;">
            🔊 You said:
        </p>
        <p style="font-size: 24px; margin-bottom: 16px; font-family: sans-serif; text-align: center;">
            {input_text}
        </p>
        <p style="font-size: 18px; margin-bottom: 16px; font-family: sans-serif; text-align: center; color: #666;">
            👨‍🔧 Check back for an easier way to find <em>good</em> concerts in Denver, CO.
        </p>
        <p style="text-align: center;"><a href="/">Try Again</a>
    '''

    data = {
        "title": "User Input",
        "content": content
    }
    return render_template('index.html', data=data)


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
    return jsonify(grouped_concerts)


def group_concerts(concerts) -> dict:
    '''
    Groups the concerts by date
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
