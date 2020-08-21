"""
Module for generating sub-regions within the University of Texas area and scoring
each sub-region based on its criminal activity within a specified time frame.
"""


def subregion_lats(decimal_places):
    """
    :param decimal_places:
    :return:
    """
    bottom = round(30.282200, decimal_places)
    top = round(30.299402, decimal_places)
    start = str(bottom)
    start = start[3:]
    start = int(start)
    end = str(top)
    end = end[3:]
    end = int(end)
    lats = range(start, end+1)
    points = []
    for num in lats:
      point = '30.' + str(num)
      point = float(point)
      points.append(point)
    return points


def subregion_lngs(decimal_places):
    right = round(-97.728456, decimal_places)
    left = round(-97.754840, decimal_places)
    start = str(right)
    start = start[4:]
    start = int(start)
    end = str(left)
    end = end[4:]
    end = int(end)
    lngs = range(start, end+1)
    points = []
    for num in lngs:
      point = '-97.' + str(num)
      point = float(point)
      points.append(point)
    return points


def generate_subregions(initial_weight):
    lats = subregion_lats(3)
    lngs = subregion_lngs(3)
    subregions = {}
    for i in range(len(lats)):
        for j in range(len(lngs)):
            subregions[(lats[i], lngs[j])] = initial_weight

    return subregions


def generate_subregion_weights(crime_data, crime_weights):
    """
    :param crime_data: Austin crime data - type: CrimeData object
    :param crime_weights: weights for each crime classification - type: dictionary
    :return:
    """
    # initialize weights to zero
    subregion_weights = generate_subregions(0)
    num_of_crimes = crime_data.crime_count()
    dataset = crime_data.df
    dataset['latitude'] = dataset['latitude'].astype('float')
    dataset['longitude'] = dataset['longitude'].astype('float')
    for i in range(num_of_crimes):
        lat = round(dataset['latitude'][i], 3)
        lng = round(dataset['longitude'][i], 3)
        subregion = (lat, lng)
        crime_type = dataset['crime_type'][i]
        subregion_weights[subregion] += crime_weights[crime_type]

    return subregion_weights
