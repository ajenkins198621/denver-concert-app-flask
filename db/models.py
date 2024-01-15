#!/usr/bin/env python3
'''
Database models
'''

from datetime import datetime
from flask import Flask
from db.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///denver_concerts.db'
db.init_app(app)


class ConcertRaw(db.Model):
    '''
    ConcertRaw Model
    '''

    __tablename__ = 'concert_raw'

    id = db.Column(db.Integer, primary_key=True)
    raw = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow())

    def __repr__(self):
        return f'<ConcertRaw id={self.id}>'


# class Concert(db.Model):
#     '''
#     Concert Model
#     '''

#     __tablename__ = 'concert'

#     id = db.Column(db.Integer, primary_key=True)
#     image = db.Column(db.String(200), nullable=False)
#     title = db.Column(db.String(200), nullable=False)
#     venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
#     date = db.Column(db.String(200), nullable=False)
#     created_at = db.Column(db.String(200), nullable=False,
#                            default=datetime.utcnow())

#     def __repr__(self):
#         return f'<Concert id={self.id}, image={self.image}, title={self.title}>'


# class Venue(db.Model):
#     '''
#     Venue Model
#     '''

#     __tablename__ = 'venue'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     address1 = db.Column(db.String(200), nullable=True)
#     address2 = db.Column(db.String(200), nullable=True)
#     city = db.Column(db.String(200), nullable=True)
#     state = db.Column(db.String(200), nullable=True)
#     zipcode = db.Column(db.String(200), nullable=True)
#     created_at = db.Column(db.String(200), nullable=False,
#                            default=datetime.utcnow())

#     def __repr__(self):
#         return f'<Venue id={self.id}, name={self.name}>'


# class Artist(db.Model):
#     '''
#     Artist Model
#     '''

#     __tablename__ = 'artist'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
#     sub_grenre_id = db.Column(
#         db.Integer, db.ForeignKey('genre.id'), nullable=True)
#     created_at = db.Column(db.String(200), nullable=False,
#                            default=datetime.utcnow())

#     def __repr__(self):
#         return f'<Artist id={self.id}, name={self.name}>'


# class ConcertArtist(db.Model):
#     '''
#     Concert Artist Model
#     '''

#     __tablename__ = 'concert_artist'

#     id = db.Column(db.Integer, primary_key=True)
#     concert_id = db.Column(db.Integer, db.ForeignKey(
#         'concert.id'), nullable=False)
#     artist_id = db.Column(db.Integer, db.ForeignKey(
#         'artist.id'), nullable=False)
#     created_at = db.Column(db.String(200), nullable=False,
#                            default=datetime.utcnow())

#     def __repr__(self):
#         return f'<ConcertArtist id={self.id}, concert_id={self.concert_id}, artist_id={self.artist_id}>'


# class Genre(db.Model):
#     '''
#     Genre Model
#     '''

#     __tablename__ = 'genre'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     created_at = db.Column(db.String(200), nullable=False,
#                            default=datetime.utcnow())

#     def __repr__(self):
#         return f'<Genre id={self.id}, name={self.name}>'
