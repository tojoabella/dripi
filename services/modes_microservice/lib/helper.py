import math

def radius_earth():
    return 6378137

def degrees_to_radians(degrees):
    return degrees*math.pi/180

def vector_decomposition(distance, direction, dir_deg = False):
    """
    :param direction: angle from north clockwise
    :param distance: in meters
    """
    if dir_deg:
        direction = degrees_to_radians(direction)
        slope = math.tan(direction)
    else:
        slope = math.tan(direction)



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

def radians_to_degrees(radians):
    return radians*180/math.pi

def direction_finder_rad(lat1, lon1, lat2, lon2):
    """
    radians from north, clockwise
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
    deg = radians_to_degrees(rad)
    #quadrants
    if dy < 0 and dx < 0:
        deg = 180 + deg
    elif dy < 0 and dx > 0:
        deg = 180 + deg
    elif dy > 0 and dx < 0:
        deg = 360 + deg
    return deg

print(degrees_to_radians(720))