import pandas as pd


def generate_crime_weights(crime_dataset):
    """
    :param crime_dataset: Austin crime data - type: pandas dataframe
    :return: weights on a scale of 0 to 100 for each type of crime - type: dictionary
    """
  
    crime_dataset['crime_type'] = pd.Categorical(crime_dataset['crime_type'])
    crime_weights = {}
  
    # initialize all crimes to weight of zero
    for crime in crime_dataset['crime_type'].cat.categories:
        crime_weights[crime] = 0

    # set crime weights
    crime_weights['AGG ASSAULT'] = 100
    crime_weights['AGG ROBBERY/DEADLY WEAPON'] = 100
    crime_weights['ASSAULT BY CONTACT'] = 90
    crime_weights['ASSAULT BY THREAT'] = 50
    crime_weights['ASSAULT ON PUBLIC SERVANT'] = 80
    crime_weights['ASSAULT W/INJURY-FAM/DATE VIOL'] = 80
    crime_weights['ASSAULT WITH INJURY'] = 100
    crime_weights['AUTO THEFT'] = 90
    crime_weights['BOMB THREAT'] = 70
    crime_weights['BURGLARY NON RESIDENCE'] = 90
    crime_weights['BURGLARY OF RESIDENCE'] = 90
    crime_weights['BURGLARY OF VEHICLE'] = 90
    crime_weights['CAMPING IN PARK'] = 40
    crime_weights['CRASH/FAIL STOP AND RENDER AID'] = 40
    crime_weights['CRED CARD ABUSE - OTHER'] = 10
    crime_weights['CRED CARD ABUSE BY FORGERY'] = 10
    crime_weights['CRIMINAL MISCHIEF'] = 70
    crime_weights['CRIMINAL TRESPASS'] = 50
    crime_weights['CRIMINAL TRESPASS/TRANSIENT'] = 50
    crime_weights['CRUELTY TO ANIMALS'] = 10
    crime_weights['CUSTODY ARREST TRAFFIC WARR'] = 10
    crime_weights['DAMAGE CITY PROP'] = 40
    crime_weights['DATING DISTURBANCE'] = 50
    crime_weights['DISTURBANCE - OTHER'] = 50
    crime_weights['DOC EXPOSURE'] = 70
    crime_weights['DOC FIGHTING'] = 70
    crime_weights['DOC UNREASONABLE NOISE'] = 30
    crime_weights['DOC WINDOW PEEPING - PUB AREA'] = 30
    crime_weights['DOC WINDOW PEEPING-RESIDENCE'] = 40
    crime_weights['DUI - AGE 17 TO 20'] = 70
    crime_weights['DWI 2ND'] = 70
    crime_weights['DWI'] = 70
    crime_weights['EVADING VEHICLE'] = 50
    crime_weights['EXPLOSIVE ORDNANCE DISPOSAL'] = 50
    crime_weights['FAILURE TO IDENTIFY'] = 10
    crime_weights['FAMILY DISTURBANCE'] = 20
    crime_weights['FELONY ENHANCEMENT/ASSLT W/INJ'] = 100
    crime_weights['FRAUD - OTHER'] = 10
    crime_weights['GRAFFITI'] = 40
    crime_weights['HARASSMENT OF A PUBLIC SERVANT'] = 80
    crime_weights['HARASSMENT'] = 80
    crime_weights['HAZING'] = 30
    crime_weights['IDENTITY THEFT'] = 10
    crime_weights['IMPERSONATING PUBLIC SERVANT'] = 50
    crime_weights['INDECENT EXPOSURE'] = 70
    crime_weights['LIQUOR LAW VIOLATION/OTHER'] = 60
    crime_weights['LITTERING'] = 20
    crime_weights['POSS CONTROLLED SUB/NARCOTIC'] = 50
    crime_weights['POSS OF ALCOHOL - AGE 17 TO 20'] = 20
    crime_weights['POSS OF DRUG PARAPHERNALIA'] = 40
    crime_weights['POSS/PROMO CHILD PORNOGRAPHY'] = 60
    crime_weights['POSSESSION OF MARIJUANA'] = 40
    crime_weights['PROTECTIVE ORDER'] = 30
    crime_weights['PROWLER'] = 50
    crime_weights['PUBLIC INTOXICATION'] = 50
    crime_weights['RECKLESS CONDUCT'] = 50
    crime_weights['RECKLESS DAMAGE'] = 60
    crime_weights['RESISTING ARREST OR SEARCH'] = 40
    crime_weights['ROBBERY BY ASSAULT'] = 100
    crime_weights['ROBBERY BY THREAT'] = 100
    crime_weights['SIT AND LIE ORDINANCE VIOL'] = 30
    crime_weights['STALKING'] = 70
    crime_weights['SUSPICIOUS PERSON'] = 50
    crime_weights['TERRORISTIC THREAT'] = 60
    crime_weights['TERRORISTIC THREAT-FAM/DAT VIO'] = 60
    crime_weights['THEFT BY CHECK'] = 10
    crime_weights['THEFT BY SHOPLIFTING'] = 30
    crime_weights['THEFT FROM AUTO'] = 60
    crime_weights['THEFT FROM PERSON'] = 90
    crime_weights['THEFT OF AUTO PARTS'] = 60
    crime_weights['THEFT OF BICYCLE'] = 60
    crime_weights['THEFT OF LICENSE PLATE'] = 50
    crime_weights['THEFT OF METAL'] = 40
    crime_weights['THEFT OF SERVICE'] = 20
    crime_weights['THEFT OF TRAILER'] = 50
    crime_weights['THEFT'] = 70
    crime_weights['UNLAWFUL CARRYING WEAPON'] = 60
    crime_weights['UNLAWFUL RESTRAINT'] = 70
    crime_weights['URINATING IN PUBLIC PLACE'] = 50
    crime_weights['VIOL CITY ORDINANCE - WRECKER'] = 30
    crime_weights['VIOL OF COURT ORDER-NON EPO-PO'] = 30
    crime_weights['VIOL OF EMERG PROTECTIVE ORDER'] = 40
    crime_weights['VIOL OF PARK CURFEW'] = 30
    crime_weights['VIOL STATE LAW - OTHER'] = 30
    crime_weights['VOCO - ALCOHOL  CONSUMPTION'] = 30
    crime_weights['VOCO AMPLIFIED MUSIC/VEHICLE'] = 30
    crime_weights['WARRANT ARREST NON TRAFFIC'] = 40

    return crime_weights
