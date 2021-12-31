import math

def radius_earth():
    return 6378137

def vector_decomposition(distance, direction):
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

def direction_finder(lat1, lon1, lat2, lon2):
    """
    degrees from north, clockwise
    """
    dy = lat2 - lat1
    dx = lon2 - lon1
    #undefined when dy is 0
    if dy == 0 and dx > 0:
        return 90
    elif dy == 0 and dx < 0:
        return 270
    elif dy < 0 and dx == 0:
        return 180
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
    
print(direction_finder(0, 0, 0, -1))