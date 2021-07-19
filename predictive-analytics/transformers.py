import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es') # transform day to Spanish day due to days dictionary
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
    #The latitude must be a number between -90 and 90 and the longitude between -180 and 180
    if -90 <= int(lat) <= 90 and -180 <= int(lon) <= 180:
        print('Geo OK')
        return lat, lon
    else:
        print('Geo No OK')
        return 'Error'

def transform_town(town):
    if town in dictionaries.towns:
        print('Town OK')
        return dictionaries.towns[town]
    else:
        print('Town No OK')
        return -1

def transform_time(time):
    if 0 <= int(str(time)[:2]) <= 24:
        print('Time OK')
        return str(time)[:2]
    else:
        print('Time No OK')
        return -1
    