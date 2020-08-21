def load_data():
    socrata_token = 'xty4xwyMTY7JsNGnat7Av9sQt'

    dataset_id = 'fdj4-gpfu'
    domain = 'data.austintexas.gov'

    # UT austin region: latitude and longitude
    top_left = (30.299402, -97.754840)
    bottom_right = (30.282200, -97.728456)
    UTregion = [top_left, bottom_right]

    api_key = 'AIzaSyDmKbjLrlWQowWVzzTy_AAWsFQO4Hdbeko'
    utcrime = CrimeData(UTregion, api_key)
    utcrime.load(dataset_id, domain, socrata_token, 2016, 2030, 10000)
    return utcrime
