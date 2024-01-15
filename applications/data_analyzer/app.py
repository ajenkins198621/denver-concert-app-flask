# COMING SOON!

# GET DATA FROM DATABASE (concert_raw)

# for concert in concerts["_embedded"]["events"]:

#     # Concerts
#     concert_name = ""
#     concert_image = ""
#     concert_ticketmaster_id = ""
#     concert_date = ""
#     concert_time = ""

#     # Venues
#     venue_ticketmaster_id = ""
#     venue_name = ""
#     venue_image = ""
#     venue_address_1 = ""
#     venue_city = ""
#     venue_state = ""
#     venue_zip = ""

#     # Artists
#     artists = []

#     concert_name = concert['name']
#     concert_ticketmaster_id = concert['id']

#     if "images" in concert and len(concert["images"]) > 0:
#         concert_image = concert['images'][0]['url']

#     if "_embedded" in concert:
#         if "venues" in concert["_embedded"]:
#             venue = concert["_embedded"]["venues"][0]
#             venue_ticketmaster_id = venue['id']
#             venue_name = venue['name']
#             venue_address_1 = venue['address']['line1']
#             venue_city = venue['city']['name']
#             venue_state = venue['state']['stateCode']
#             venue_zip = venue['postalCode']
#             if "images" in venue and len(venue["images"]) > 0:
#                 venue_image = venue['images'][0]['url']

#         if "attractions" in concert["_embedded"] and len(concert["_embedded"]["attractions"]) > 0:
#             concert_artists = concert["_embedded"]["attractions"]
#             for artist in concert_artists:
#                 artist_ticketmaster_id = ""
#                 artist_name = ""
#                 artist_spotify_url = ""
#                 artist_image = ""

#                 artist_ticketmaster_id = artist['id']
#                 artist_name = artist['name']
#                 if "externalLinks" in artist:
#                     if "spotify" in artist["externalLinks"] and len(artist["externalLinks"]['spotify']) > 0:
#                         artist_spotify_url = artist["externalLinks"]['spotify'][0]['url']
#                 if "images" in artist and len(artist["images"]) > 0:
#                     artist_image = artist['images'][0]['url']

#     if "dates" in concert:
#         concert_date = concert['dates']['start']['localDate']
#         concert_time = concert['dates']['start']['localTime']

#     concerts_html += f"<hr />"
#     concerts_html += f"<p>{concert_name} (Ticketmaster ID: {concert_ticketmaster_id})</p>"
#     concerts_html += f"<img src='{concert_image}' style='max-width: 250px;' />"
#     concerts_html += f"<p>{concert_date} {concert_time}</p>"

#     concerts_html += f"<p>{venue_name} (Ticketmaster ID: {venue_ticketmaster_id})</p>"
#     concerts_html += f"<img src='{venue_image}' style='max-width: 250px;' />"
#     concerts_html += f"<p>{venue_address_1}</p>"
#     concerts_html += f"<p>{venue_city}, {venue_state} {venue_zip}</p>"

#     for artist in artists:
#         artist_name = ""
#         artist_spotify_url = ""
#         artist_image = ""

#         artist_name = artist['name']
#         if "externalLinks" in artist:
#             if "spotify" in artist["externalLinks"] and len(artist["externalLinks"]['spotify']) > 0:
#                 artist_spotify_url = artist["externalLinks"]['spotify'][0]['url']
#         if "images" in artist and len(artist["images"]) > 0:
#             artist_image = artist['images'][0]['url']

#         concerts_html += f"<p>{artist_name} (Spotify URL: {artist_spotify_url})</p>"
#         concerts_html += f"<img src='{artist_image}' style='max-width: 250px;' />"

# return concerts_html
