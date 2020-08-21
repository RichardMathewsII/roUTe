from gmplot import gmplot


def visualize_routes(point_routes, user_location, destination, same_map=True):
    colors = ['#ff0000', '#fffb00', '#ffa200', '#3cff00', '#00fff7', '#00b7ff', '#0000ff', '#9000ff',
              '#f700ff', '#ff008c', '#050404', '#b2bf8a', '#f700ff', '#ff008c', '#050404', '#b2bf8a']
    if same_map:
        gmap = gmplot.GoogleMapPlotter(pointA[0], pointA[1], zoom=15, apikey=api_key)
        for i in range(len(point_routes)):
            lats = point_routes[i]['latitudes']
            lngs = point_routes[i]['longitudes']
            gmap.scatter(lats, lngs, colors[i], size=5, marker=False)
        gmap.draw('routes.html')
    else:
        for i in range(len(point_routes)):
            gmap = gmplot.GoogleMapPlotter(pointA[0], pointA[1], zoom=15, apikey=api_key)
            lats = point_routes[i]['latitudes']
            lngs = point_routes[i]['longitudes']
            gmap.scatter(lats, lngs, colors[i], size=5, marker=False)
            gmap.draw('route' + str(i) + '.html')
