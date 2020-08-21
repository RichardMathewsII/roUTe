from crime_data import *
from crime_weights import *
from load_data import *
from regions import *
from routes import *
from score import *
import googlemaps
from googlemaps import directions
from googlemaps import client
from googlemaps import roads
from googlemaps import convert
import pandas as pd
from sodapy import Socrata


def main(user_location, destination):
    """
    Returns polyline of safest route
    :param user_location: list or tuple of latitude, longitude coordinates (lat, lng)
    :param destination: list or tuple of latitude, longitude coordinates(lat, lng)
    :return:
    """
    utcrime = load_data()
    crime_weights = generate_crime_weights(utcrime.df)
    subregion_weights = generate_subregion_weights(utcrime, crime_weights)
    api_key = 'AIzaSyDmKbjLrlWQowWVzzTy_AAWsFQO4Hdbeko'
    cli = client.Client(key=api_key)
    gmap_routes = route_generator(user_location, destination, cli)
    point_routes = convert_to_point_routes(gmap_routes)
    scores = score_routes(point_routes, gmap_routes, subregion_weights)
    safe_route = safest_route(scores)
    route = gmap_routes[safe_route]
    if type(route) is dict:
        # alternative route, indexes differently than waypoint route
        polyline = route['overview_polyline']['points']
    else:
        # waypoint route, indexes differently than alternative route
        polyline = route[0]['overview_polyline']['points']

    return polyline
