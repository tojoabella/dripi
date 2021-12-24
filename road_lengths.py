import os
import googlemaps
import road_identity


def road_length(lat, lon):
    road = road_identity.get_street(lat, lon)
    print(road)

    
lat, lon = 21.321789, -157.879638
road_length(lat, lon)