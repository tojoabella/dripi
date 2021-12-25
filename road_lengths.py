import os
import googlemaps
import road_identity


def road_length(lat, lon):
    road = road_identity.get_street(lat, lon)
    