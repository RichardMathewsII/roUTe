import googlemaps
from googlemaps import directions
from googlemaps import client
from googlemaps import roads
from googlemaps import convert


def points(pointA, pointB, num):
    lat_distance = pointB[0] - pointA[0]
    lng_distance = pointB[1] - pointA[1]
    lats = [pointA[0]]
    lngs = [pointA[1]]
    interm_points = []
    for i in range(1, num+1):
      lat = pointA[0] + lat_distance * (i / (num + 1))
      lng = pointA[1] + lng_distance * (i / (num + 1))
      interm_points.append((lat, lng))
      lats.append(lat)
      lngs.append(lng)
    lats.append(pointB[0])
    lngs.append(pointB[1])
    return interm_points, lats, lngs


def waypoint_generator(user_location, destination, client):
    pointA = user_location
    pointB = destination
    interm, _, _ = points(pointA, pointB, 3)
    slope = (pointA[0] - pointB[0]) / (pointA[1] - pointB[1])
    perp_slope = -slope ** (-1)
    distance = ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) ** (0.5)

    # ROUND 1
    d = distance * 0.1
    point1 = ((interm[0][0] + perp_slope * d), (interm[0][1] + d))
    point2 = ((interm[0][0] - perp_slope * d), (interm[0][1] - d))
    point3 = ((interm[2][0] + perp_slope * d), (interm[2][1] + d))
    point4 = ((interm[2][0] - perp_slope * d), (interm[2][1] - d))
    gm_waypoints = roads.nearest_roads(client, [point1, point2, point3, point4])
    # print(gm_waypoints)
    waypoints = []
    for i in range(1, 5):
        lat = gm_waypoints[i]['location']['latitude']
        lng = gm_waypoints[i]['location']['longitude']
        waypoints.append((lat, lng))

    # ROUND 2
    d = distance * 0.2
    point1 = ((interm[0][0] + perp_slope * d), (interm[0][1] + d))
    point2 = ((interm[0][0] - perp_slope * d), (interm[0][1] - d))
    point3 = ((interm[2][0] + perp_slope * d), (interm[2][1] + d))
    point4 = ((interm[2][0] - perp_slope * d), (interm[2][1] - d))
    gm_waypoints = roads.nearest_roads(client, [point1, point2, point3, point4])
    # print(gm_waypoints)
    for i in range(1, 5):
        lat = gm_waypoints[i]['location']['latitude']
        lng = gm_waypoints[i]['location']['longitude']
        waypoints.append((lat, lng))
    return waypoints


def route_generator(user_location, destination, client):
    pointA = user_location
    pointB = destination
    cli = client
    wp = waypoint_generator(pointA, pointB, cli)
    gmap_routes = []
    route = directions.directions(cli, pointA, pointB, mode='walking', alternatives=True)
    print(len(route))
    for i in range(len(route)):
        gmap_routes.append(route[i])
    for waypoint in wp:
        route = directions.directions(cli, pointA, pointB, mode='walking', waypoints=waypoint)
        gmap_routes.append(route)
    gmap_routes.append(directions.directions(cli, pointA, pointB, mode='walking', waypoints=[wp[0], wp[2]]))
    gmap_routes.append(directions.directions(cli, pointA, pointB, mode='walking', waypoints=[wp[0], wp[3]]))
    gmap_routes.append(directions.directions(cli, pointA, pointB, mode='walking', waypoints=[wp[1], wp[2]]))
    gmap_routes.append(directions.directions(cli, pointA, pointB, mode='walking', waypoints=[wp[1], wp[3]]))
    return gmap_routes


def convert_to_point_routes(map_routes):
    point_routes = []
    for route in map_routes:
        lats = []
        lngs = []
        if type(route) is dict:
            # alternative route, indexes differently than waypoint route
            polyline = route['overview_polyline']['points']
        else:
            # waypoint route, indexes differently than alternative route
            polyline = route[0]['overview_polyline']['points']
        route_points = convert.decode_polyline(polyline)
        for i in range(len(route_points) - 1):
            if i == 0:
                prev = (route_points[i]['lat'], route_points[i]['lng'])
                proceed = True
            if i > 0:
                pointA = (route_points[i]['lat'], route_points[i]['lng'])
                euclidean_distance = ((pointA[0] - prev[0]) ** 2 + (pointA[1] - prev[1]) ** 2) ** 0.5
                if euclidean_distance > 0.0002:
                    proceed = True
                    prev = pointA
                else:
                    proceed = False
            if proceed:
                pointA = (route_points[i]['lat'], route_points[i]['lng'])
                lats.append(pointA[0])
                lngs.append(pointA[1])
                pointB = (route_points[i + 1]['lat'], route_points[i + 1]['lng'])
                # print(pointB)
                # pointB = (legs[i+1][0]['lat'], legs[i+1][0]['lng'])
                # print(pointB)
                euclidean_distance = ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) ** 0.5
                num = int(euclidean_distance // 0.0004) - 1
                if num > 0:
                    interm, _, _ = points(pointA, pointB, num)
                    for x in interm:
                        lats.append(x[0])
                        lngs.append(x[1])

        lats.append(pointB[0])
        lngs.append(pointB[1])
        point_routes.append({'latitudes': lats, 'longitudes': lngs})

    return point_routes
