import math

def new_points(lat, lon, distance, direction):
    #https://stackoverflow.com/questions/7477003/calculating-new-longitude-latitude-from-old-n-meters
    r_earth = 6378137
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
    new_lat  = lat  + (dy/r_earth) * (180/math.pi)
    new_lon = lon + (dx/r_earth) * (180/math.pi)/math.cos(lat*math.pi/180)
    return new_lat, new_lon
