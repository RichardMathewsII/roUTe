"""
Module for scoring point routes and selecting the route optimized for safety and speed.
"""


def extract_duration(route):
    """
    Pull the duration of the route from a GoogleMaps route
    """
    duration = 0
    if type(route) is list:
        route = route[0]
    for leg in range(len(route['legs'])):
        duration += route['legs'][leg]['duration']['value']
    return duration


def average_duration(map_routes):
    """
    Compute the average duration of all routes
    """
    durations = []
    for i in range(len(map_routes)):
        durations.append(extract_duration(map_routes[i]))
    sum_ = 0
    for dur in durations:
        sum_ += dur
    avg_duration = sum_ / len(durations)
    return avg_duration


def score_routes(point_routes, map_routes, subregion_weights):
    """
    Score each route, 90% based on safety, 10% based on time
    """
    scores = {}
    idx = 0
    avg_duration = average_duration(map_routes)
    for route in point_routes:
        lats = [round(float(lat), 3) for lat in route['latitudes']]
        lngs = [round(float(lng), 3) for lng in route['longitudes']]
        sum_ = 0
        for i in range(len(lats)):
            sum_ += subregion_weights[(lats[i], lngs[i])]
        avg = sum_ / len(lats)
        duration = extract_duration(map_routes[idx])
        score = 0.9 * avg + 0.1 * avg * (duration / avg_duration)
        scores[idx] = score
        idx += 1

    return scores


def safest_route(scores):
    """
    Selects the route with the lowest score to be safest route
    """
    prev = (0, scores[0])
    for i in range(1, len(scores)):
        if scores[i] < prev[1]:
            prev = (i, scores[i])
    winner = prev[0]
    return winner
