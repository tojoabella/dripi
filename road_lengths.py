import os
import googlemaps
import road_identity

def road_length(lat, lon):
    street = road_identity.get_street(lat, lon)