import math

def radius_earth():
    return 6378137

def degrees_to_radians(degrees):
    return degrees*math.pi/180

def radians_to_degrees(radians):
    return radians*180/math.pi

def distance_calculator(lat2, lon2, lat1, lon1):
    #https://cloud.google.com/blog/products/maps-platform/how-calculate-distances-map-maps-javascript-api
    r = 6371071
    lat2 = lat2 * (math.pi/180)
    lat1 = lat1 * (math.pi/180)
    difflat = lat2 - lat1
    difflon = (lon2 - lon1) * (math.pi/180)
    d = 2 * r * math.asin(math.sqrt(math.sin(difflat/2)*math.sin(difflat/2)+math.cos(lat1)*math.cos(lat2)*math.sin(difflon/2)*math.sin(difflon/2)))
    return d


def vector_decomposition_2(distance, direction):
    if direction == 'N':
        dy = distance
        dx = 0
    elif direction == 'NE':
        dy = distance/math.sqrt(2)
        dx = distance/math.sqrt(2)
    elif direction == 'E':
        dy = 0
        dx = distance
    elif direction == 'SE':
        dy = -distance/math.sqrt(2)
        dx = distance/math.sqrt(2)
    elif direction == 'S':
        dy = -distance
        dx = 0
    elif direction == 'SW':
        dy = -distance/math.sqrt(2)
        dx = -distance/math.sqrt(2)
    elif direction == 'W':
        dy = 0
        dx = -distance
    elif direction == 'NW':
        dy = distance/math.sqrt(2)
        dx = -distance/math.sqrt(2)
    else:
        return None
    
    return dy, dx

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
    deg = radians_to_degrees(rad)
    #quadrants
    if dy < 0 and dx < 0:
        deg = 180 + deg
    elif dy < 0 and dx > 0:
        deg = 180 + deg
    elif dy > 0 and dx < 0:
        deg = 360 + deg
    return deg