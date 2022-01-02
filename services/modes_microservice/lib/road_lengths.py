import math
from services.modes_microservice.lib.location_identifiers import locationIdentifiers
import services.modes_microservice.lib.helper as helper
from services.modes_microservice.lib.gmaps_api import GMaps

def new_points(lat, lon, distance, direction):
    #https://stackoverflow.com/questions/7477003/calculating-new-longitude-latitude-from-old-n-meters
    r_earth = helper.radius_earth()
    dy, dx = helper.vector_decomposition(distance, direction)
    new_lat  = lat  + (dy/r_earth) * (180/math.pi)
    new_lon = lon + (dx/r_earth) * (180/math.pi)/math.cos(lat*math.pi/180)
    return new_lat, new_lon

def road_length(lat, lon):
    #get current road and id
    road = locationIdentifiers.get_road(lat, lon)
    for k, v in road.items():
        name = k
        id = v
    #test nearby points



    