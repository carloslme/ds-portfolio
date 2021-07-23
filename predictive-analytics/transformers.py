import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_ES') # transform day to Spanish day due to days dictionary
import dictionaries

def transform_day(date):
    """ This function transforms a date and return a number

    Args:
        date (string): Date in format 2021-07-18

    Returns:
        int: number defined in days dictionary
    """    
    # parsing date to datetime
    year, month, day = (int(x) for x in date.split('-'))    
    ans = datetime.date(year, month, day)
    key = ans.strftime("%A").capitalize() 

    # get key of day from data dictionary using day in Spanish
    if key in dictionaries.days:
        print('Day OK')
        return dictionaries.days[key]
    else:
        print('Day No OK')
        return -1 

def transform_geo(lat, lon):
    """This function tranform the latitude and longitude, it also evaluates if the number between ranges.txt
       The latitude must be a number between -90 and 90 and the longitude between -180 and 180

    Args:
        lat (string): The people latitude
        lon (string): The people longitude

    Raises:
        ValueError: If the latitude or longitude are not in the defined ranges.

    Returns:
        Two values: The latitude and longitude checked.
    """    

    if -90 <= float(lat) <= 90 and -180 <= float(lon) <= 180:
        print('Geo OK')
        return lat, lon
    else:
        print('Geo No OK')
        raise ValueError 

def transform_town(town):
    """This function evaluates if the town received is in the approved towns list.

    Args:
        town (string): Town selected in the UI.

    Returns:
        string: Value defined and corresponding in the towns dictionary.
    """    

    if town in dictionaries.towns:
        print('Town OK')
        return dictionaries.towns[town]
    else:
        print('Town No OK')
        return -1

def transform_time(time):
    """This function transforms the time in format H:M and extracts just the hour, for example: 19:23 to 19

    Args:
        time (string): Time selected in the UI.

    Returns:
        string: Just the hour.
    """    
    if 0 <= int(str(time)[:2]) <= 24:
        print('Time OK')
        return str(time)[:2]
    else:
        print('Time No OK')
        return -1
    