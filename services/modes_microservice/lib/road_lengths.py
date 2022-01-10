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

def direction_finder_rad(lat2, lon2, lat1, lon1):
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


def direction_finder_deg(lat2, lon2, lat1, lon1):
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

def distance_calculator(lat2, lon2, lat1, lon1):
    #https://cloud.google.com/blog/products/maps-platform/how-calculate-distances-map-maps-javascript-api
    r = 6371071
    lat2 = lat2 * (math.pi/180)
    lat1 = lat1 * (math.pi/180)
    difflat = lat2 - lat1
    difflon = (lon2 - lon1) * (math.pi/180)
    d = 2 * r * math.asin(math.sqrt(math.sin(difflat/2)*math.sin(difflat/2)+math.cos(lat1)*math.cos(lat2)*math.sin(difflon/2)*math.sin(difflon/2)))
    return d

def nearest_road_attempt(lat, lon, road_name, direction, distance=10, attempts=8):
    denominator = attempts/2
    for attempt in range(0, attempts):
        #get attempt direction, then attempt point
        if attempt == 0:
            numerator = 0
        elif attempt%2 == 0:
            numerator = (attempts - attempt/2)*math.pi
        else:
            numerator = (int(attempt/2) + 1)*math.pi
        
        dir_attempt = direction + numerator/denominator
        point_attempt = new_point(lat, lon, distance, dir_attempt)
        point_attempt_result = GMaps.nearest_roads([point_attempt])
        point_name = None
        for address in point_attempt_result['address_components']:
            if 'route' in address['types']:
                point_name = address['long_name']
                break
        if point_name:
            if point_name == road_name:
                return point_attempt_result
    return None
            

def road_attempt(lat, lon, road_name, distance, direction, attempts=8):
    denominator = attempts/2
    for attempt in range(0, attempts):
        current_points = [(lat, lon)]
        #get attempt direction, then attempt point
        if attempt == 0:
            numerator = 0
        elif attempt%2 == 0:
            numerator = (attempts - attempt/2)*math.pi
        else:
            numerator = (int(attempt/2) + 1)*math.pi
        dir_attempt = direction + numerator/denominator
        point_attempt = new_point(lat, lon, distance, dir_attempt)
        current_points.append(point_attempt)
        point_attempt_result = GMaps.snap_to_roads(current_points)
        point_attempt_result = point_attempt_result[1:]
        '''
        point_attempt_distance = distance_calculator(point_attempt_result['location']['latitude'], point_attempt_result['location']['longitude'], lat, lon)
        if point_attempt_distance < distance/2.5:
            continue
        '''
        points_of_same_road = []
        for point in point_attempt_result:
            point_id = point['placeId']
            point_geocode = GMaps.reverse_geocode_place_id(point_id)[0]
            point_name = None
            for address in point_geocode['address_components']:
                if 'route' in address['types']:
                    point_name = address['long_name']
                    break
            
            if point_name:
                if point_name == road_name:
                    points_of_same_road.append(point)
                else:
                    break

        if len(points_of_same_road) > 0:
            return points_of_same_road
        
    return None

def road_length(lat, lon):
    #static
    distance = 50
    initial_lat = lat
    initial_lon = lon

    #get current road and id
    road = locationIdentifiers.get_road(lat, lon)
    road_name = road['name']
    id = road['id']

    #instantiate
    direction = 0
    road_points = [(initial_lat, initial_lon)]
    queue = [] #points to be explored
    ids = [id]
    directions = []


    #get initial
    first_attempt = nearest_road_attempt(initial_lat, initial_lon, road_name, direction)
    if first_attempt:
        first_attempt_lat = first_attempt['location']['latitude']
        first_attempt_lon = first_attempt['location']['longitude']
        one_way_test = [(initial_lat, initial_lon), (first_attempt_lat, first_attempt_lon)]
        if len(GMaps.snap_to_roads(one_way_test)) == 1:
            return "one way street foing from first attempt to given point"
        one_way_test = [(first_attempt_lat, first_attempt_lon), (initial_lat, initial_lon)]
        if len(GMaps.snap_to_roads(one_way_test)) == 1:
            return "one way street going from first attempt to initial point"

        direction = direction_finder_rad(first_attempt_lat, first_attempt_lon, initial_lat, initial_lon)
    else:
        return "not a road"

    initial_1 = road_attempt(lat, lon, road_name, distance, direction)
    if initial_1:
        for i in range(len(initial_1)):
            direction = direction_finder_rad(initial_1[i]['location']['latitude'], initial_1[i]['location']['longitude'], lat, lon)
            lat = initial_1[i]['location']['latitude']
            lon = initial_1[i]['location']['longitude']
            road_points.append((lat, lon))
            directions.append(direction)
            if i == len(initial_1) - 1:
                queue.append((lat, lon, direction))
                lat = initial_lat
                lon = initial_lon
    
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
            queue.append((attempt_lat, attempt_lon, direction))
    '''
    initial_2 = road_attempt(lat, lon, road_name, distance, direction + math.pi)
    if initial_2:
        for i in range(len(initial_2)):
            direction = direction_finder_rad(initial_2[i]['location']['latitude'], initial_2[i]['location']['longitude'], lat, lon)
            lat = initial_2[i]['location']['latitude']
            lon = initial_2[i]['location']['longitude']
            road_points.append((lat, lon))
            directions.append(direction)
            if i == len(initial_2) - 1:
                queue.append((lat, lon, direction))
                lat = initial_lat
                lon = initial_lon
    '''


#road_length(21.364075, -158.077205)
road_length(40.805514, -73.964001)