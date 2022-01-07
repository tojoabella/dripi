import math
from services.modes_microservice.lib.location_identifiers import locationIdentifiers
from services.modes_microservice.lib.location_identifiers import GMaps

import services.modes_microservice.lib.helper as helper

def vector_decomposition(distance, direction, dir_deg = False):
    """
    given a distance and a direction, get dx and dy

    :param numerical direction: angle from north clockwise
    :param numerical distance: in meters
    :param bool dir_deg: direction given in degrees (over radians)

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

def new_point(lat, lon, distance, direction, dir_deg = False):
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

def direction_finder_rad(lat1, lon1, lat2, lon2):
    """
    given point1 and point2, get the direction from point1 to point2

    :param numerical lat1: latitude of point1
    :param numerical lon1: longitude of point1
    :param numerical lat2: latitude of point2
    :param numerical lon2: longitude of point2

    :return numerical rad: angle in radians clockwise from north
    """
    dy = lat2 - lat1
    dx = lon2 - lon1
    #undefined when dy is 0
    if dy == 0 and dx == 0:
        return None
    elif dy == 0 and dx > 0:
        return math.pi/2
    elif dy < 0 and dx == 0:
        return math.pi
    elif dy == 0 and dx < 0:
        return 3*math.pi/2
    rad = math.atan(dx/dy)
    #quadrants
    if dy < 0 and dx < 0:
        rad = math.pi + rad
    elif dy < 0 and dx > 0:
        rad = math.pi + rad
    elif dy > 0 and dx < 0:
        rad = 2*math.pi + rad
    return rad


def direction_finder_deg(lat1, lon1, lat2, lon2):
    """
    degrees from north, clockwise
    """
    dy = lat2 - lat1
    dx = lon2 - lon1
    #undefined when dy is 0
    if dy == 0 and dx == 0:
        return None
    elif dy == 0 and dx > 0:
        return 90
    elif dy < 0 and dx == 0:
        return 180
    elif dy == 0 and dx < 0:
        return 270
    rad = math.atan(dx/dy)
    deg = helper.radians_to_degrees(rad)
    #quadrants
    if dy < 0 and dx < 0:
        deg = 180 + deg
    elif dy < 0 and dx > 0:
        deg = 180 + deg
    elif dy > 0 and dx < 0:
        deg = 360 + deg
    return deg


def road_attempt(lat, lon, road_name, distance, direction, attempts=8):
    current_points = [(lat, lon)]
    denominator = attempts/2
    for attempt in range(0, attempts):
        #get attempt direction, then attempt point
        if attempt%2 == 0:
            numerator = (attempts - attempt/2)*math.pi
        else:
            numerator = (int(attempt/2) + 1)*math.pi
        dir_attempt = direction + numerator/denominator
        point_attempt = new_point(lat, lon, distance, dir_attempt)
        current_points.append(point_attempt)
        snap_results = GMaps.snap_to_roads(current_points)
        point_attempt_result = snap_results[-1]
        point_attempt_result_id = point_attempt_result['placeId']
        point_attempt_result_geocode = GMaps.reverse_geocode_place_id(point_attempt_result_id)[0]
        point_attempt_result_name = None
        for address in point_attempt_result_geocode['address_components']:
            if 'route' in address['types']:
                point_attempt_result_name = address['long_name']
        
        if point_attempt_result_name:
            if point_attempt_result_name == road_name:
                return point_attempt_result
        
    return None

def road_length(lat, lon):
    #static
    distance = 25

    #get current road and id
    road = locationIdentifiers.get_road(lat, lon)
    road_name = road['name']
    id = road['id']

    #instantiate
    direction = 0
    road_points = [(lat, lon)]
    queue = [(lat, lon, direction)] #points to be explored
    ids = [id]
    directions = []

    #get initial directions
    initial = road_attempt(lat, lon, road_name, distance, 0)
    if initial:
        initial_lat = initial['location']['latitude']
        initial_lon = initial['location']['longitude']
        direction = direction_finder_rad(initial_lat, initial_lon, lat, lon)
        queue.append((initial_lat, initial_lon, direction))
        road_points.append((initial_lat, initial_lon))

    initial_2 = road_attempt(lat, lon, road_name, distance, -direction)
    if initial_2:
        initial_lat = initial_2['location']['latitude']
        initial_lon = initial_2['location']['longitude']
        direction2 = direction_finder_rad(initial_lat, initial_lon, lat, lon)
        if direction2 != direction:
            queue.append(initial_lat, initial_lon, direction2)
            road_points.append((initial_lat, initial_lon))

    #snap nearby points and see if its in the same road
    while queue: 
        lat, lon, dir = queue.pop(-1)
        #attempts
        attempt = road_attempt(lat, lon, road_name, distance, dir)
        if attempt:           
            #append to road_points
            attempt_lat = attempt['location']['latitude']
            attempt_lon = attempt['location']['longitude']
            road_points.append((attempt_lat, attempt_lon))

            #update direction and append to directions
            direction = direction_finder_rad(attempt_lat, attempt_lon, lat, lon)
            directions.append(direction)

            #append to ids
            ids.append(attempt['placeId'])

            #append to queue
            queue.append(attempt_lat, attempt_lon, direction)

            