import math
from services.modes_microservice.lib.location_identifiers import locationIdentifiers
from services.modes_microservice.lib.location_identifiers import GMaps

import cProfile

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

def test_one_way_road(lat1, lon1, lat2, lon2):
    """
    0: two-way street
    1: one way street going from first attempt to given point
    2: one way street going from first attempt to initial point
    """
    point_1_to_point_2 = [(lat1, lon1), (lat2, lon2)]
    if len(GMaps.snap_to_roads(point_1_to_point_2)) == 1:
        return 1

    point_2_to_point_1 = [(lat2, lon2), (lat1, lon1)]
    if len(GMaps.snap_to_roads(point_2_to_point_1)) == 1:
        return 2

    return 0

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
        point_attempt_result = GMaps.nearest_roads([point_attempt])[1]
        point_name = None
        point_geocode = GMaps.reverse_geocode_place_id(point_attempt_result['placeId'])[0]
        for address in point_geocode['address_components']:
            if 'route' in address['types']:
                point_name = address['long_name']
                break
        if point_name:
            if point_name == road_name:
                return point_attempt_result
    return None
            

def road_attempt(lat, lon, road_name, distance, direction, ids, attempts=8):
    """
    snap to road attempt

    :return: a list of points that have the same road names as the given road name
    """
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
        #if direction is None, then it's a dead end
        #if direction from the first point to the original point is the same as the given direction, I am going back the opposite direction
        valid_point_found = False
        first_diff_point_found = False

        points_of_same_road = []
        for point in point_attempt_result:
            point_lat = point['location']['latitude']
            point_lon = point['location']['longitude']
            point_id = point['placeId']
            if point_id in ids:
                points_of_same_road.append(point)
                if not first_diff_point_found and not valid_point_found and point_lat != lat and point_lon != lon and round(direction_finder_rad(lat, lon, point_lat, point_lon), 3) != round(direction, 3):
                    valid_point_found = True

            else:
                point_geocode = GMaps.reverse_geocode_place_id(point_id)[0]
                point_name = None
                for address in point_geocode['address_components']:
                    if 'route' in address['types']:
                        point_name = address['long_name']
                        break

                if point_name and point_name == road_name:
                    points_of_same_road.append(point)
                    if not first_diff_point_found and not valid_point_found and point_lat != lat and point_lon != lon and round(direction_finder_rad(lat, lon, point_lat, point_lon), 3) != round(direction, 3):
                        valid_point_found = True
                else:
                    break

            if point_lat != lat and point_lon != lon:
                first_diff_point_found = True

        if valid_point_found:
            return points_of_same_road
        
    return None

def verify_road_attempt(lat, lon, attempt, road_points, ids, queue):
    if attempt:
        for i in range(len(attempt)):
            #update direction
            direction = direction_finder_rad(attempt[i]['location']['latitude'], attempt[i]['location']['longitude'], lat, lon)

            #attempt may have same lat and lon but diff placeId. if same lat and lon, direction is None
            if direction:

                #append to road_points
                lat = attempt[i]['location']['latitude']
                lon = attempt[i]['location']['longitude']
                road_points.append((lat, lon))

                #append to ids
                ids.add(attempt[i]['placeId'])

            else:
                ids.add(attempt[i]['placeId'])

            #append to queue
            if i == len(attempt) - 1:
                queue.append((lat, lon, direction))
    return road_points, ids, queue

def snap_points_one_way(queue, road_points, ids, road_name, distance):
    #snap nearby points and see if its in the same road
    while queue:
        lat, lon, dir = queue.pop(-1)
        #attempts
        attempt = road_attempt(lat, lon, road_name, distance, dir, ids)
        road_points, ids, queue = verify_road_attempt(lat, lon, attempt, road_points, ids, queue)
    return road_points, ids

def two_way_road(initial_lat, initial_lon, road_name, direction, road_points, ids):
    #update distance if necessary
    if "Freeway" in road_name or "Highway" in road_name:
        distance = 1000
    elif "Street" in road_name:
        distance = 200
    else:
        print("road name is: ", road_name)
        distance = 200

    #instantiate
    queue = [(initial_lat, initial_lon, direction)]
    road_points, ids = snap_points_one_way(queue, road_points, ids, road_name, distance)

    road_points.reverse()

    queue = [(initial_lat, initial_lon, direction + math.pi)]
    road_points, ids = snap_points_one_way(queue, road_points, ids, road_name, distance)

    return road_points, ids

def road_length(lat, lon):
    initial_lat = lat
    initial_lon = lon

    #get current road name and id
    road = locationIdentifiers.get_road(lat, lon)
    road_name = road['name']
    id = road['id']

    #instantiate
    direction = 0
    road_points = [(initial_lat, initial_lon)]
    ids = {id}

    #get direction of road at inital point
    first_attempt = nearest_road_attempt(initial_lat, initial_lon, road_name, direction)
    if first_attempt:
        first_attempt_lat = first_attempt['location']['latitude']
        first_attempt_lon = first_attempt['location']['longitude']

        #test one-way street
        one_way_test = test_one_way_road(initial_lat, initial_lon, first_attempt_lat, first_attempt_lon)
        if not one_way_test:
            direction = direction_finder_rad(first_attempt_lat, first_attempt_lon, initial_lat, initial_lon)
            road_points, ids = two_way_road(initial_lat, initial_lon, road_name, direction, road_points, ids)
            return {'road_points': road_points,
                    'ids': ids}

        elif one_way_test == 1:
            return "one way street foing from first attempt to given point"
        elif one_way_test == 2:
            return "one way street going from first attempt to initial point"
    
    else:
        return "not a road"


if __name__=="__main__":
    cProfile.run('road_length(21.364075, -158.077205)')
    cProfile.run('road_length(21.364075, -158.077205)', filename="prof.out")


#print(road_length(21.364075, -158.077205))