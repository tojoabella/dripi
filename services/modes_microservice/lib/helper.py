import math

def radius_earth():
    return 6378137

def degrees_to_radians(degrees):
    return degrees*math.pi/180

def radians_to_degrees(radians):
    return radians*180/math.pi



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
