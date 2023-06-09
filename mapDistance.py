# use pip3 install googlemaps if needed 
import googlemaps
from datetime import datetime


API_KEY = ''
client = googlemaps.Client(API_KEY)


def distance_between(start, end, mode):

    # Calculate the distance between the start and end locations at the current time.
    directions_result = client.directions(start, end, mode, departure_time=datetime.now())
    # select the first 'leg' of the journey, and assign the distance value to 'distance'
    distance = directions_result[0]['legs'][0]['distance']['value']

    return distance

def time_taken(start, end, mode):

    # Calculate the distance between the start and end locations at the current time.
    directions_result = client.directions(start, end, mode, departure_time=datetime.now())
    # select the first 'leg' of the journey, and assign the distance value to 'distance'
    duration = directions_result[0]['legs'][0]['duration_in_traffic']['text']

    return duration

# https://maps.googleapis.com/maps/api/distancematrix/json
#   ?destinations=Greenwich%%
#   &origins=Stockholm%
#   &key=

# hard coded values
# mode is set to driving, but can also use walking, bicycling or transit (public transport)
mode = 'driving'
start = 'Greenwich, Greater London, UK'
end = 'Stockholm , Sweden'

# use these to input 2 locations 
# start = input("Enter your start position: ")
# end = input("Enter your destination: ")

distance = distance_between(start, end, mode)
duration = time_taken(start, end, mode)

miles = distance/1609

print(f'The distance between {start} and {end} is {distance} meters or around {round(miles)} miles')
print('The journey would take '+ duration +'.')
