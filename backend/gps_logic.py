def check_geofence(x, y, bounds):
    """
    bounds = (xmin, xmax, ymin, ymax)
    If vehicle (x,y) goes outside → return True
    """
    xmin, xmax, ymin, ymax = bounds
    if x < xmin or x > xmax or y < ymin or y > ymax:
        return True
    return False
