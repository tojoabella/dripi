import math
from services.modes_microservice.lib.location_identifiers import locationIdentifiers
import services.modes_microservice.lib.helper as helper

def vector_decomposition(distance, direction, dir_deg = False):
    """
    given a distance and a direction, get dx and dy

    :param direction: angle from north clockwise
    :param distance: in meters
    :param dir_deg: direction given in degrees (over radians)

    :return tuple of int:
        dy: change in meters north
        dx: change in meters east
    """
    if dir_deg:
        direction = helper.degrees_to_radians(direction)
    dx = math.sin(direction)*distance
    dx = round(dx)
    dy = math.cos(direction)*distance
    dy = round(dy)
    return dy, dx

def new_points(lat, lon, distance, direction, dir_deg = False):
    """
    given a point, a distance, and a direction, get a new point

    :param float lat: original point's latitude
    :param float lon: original point's longitude
    :param numerical distance: distance in meters from original point
    :param numerical direction: direction from original point
    :param dir_deg: direction in degrees (rather than radians)

    :return tuple of float:
        new_lat: new point's latitude
        new_lon: new point's longitude 
    """
    #https://stackoverflow.com/questions/7477003/calculating-new-longitude-latitude-from-old-n-meters
    r_earth = helper.radius_earth()
    dy, dx = vector_decomposition(distance, direction)
    new_lat  = lat  + (dy/r_earth) * (180/math.pi)
    new_lon = lon + (dx/r_earth) * (180/math.pi)/math.cos(lat*math.pi/180)
    return new_lat, new_lon

def road_length(lat, lon):
    #static
    distance = 25

    #get current road and id
    road = locationIdentifiers.get_road(lat, lon)
    road_name = road['name']
    id = road['id']

    current_points = []
    found_new_point = False
    #snap nearby points and see if its in the same road
    for i in range(0, 8):
        direction = i*math.pi/4
        new_lat, new_lon = new_points(lat, lon, distance, direction)
        #snap points to new road

        #if point's id is same as current road's id, add the point to current_points. get the point's direction. test the opposite direction