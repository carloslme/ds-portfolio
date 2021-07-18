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
        return dictionaries.days[key]
    else:
        return -1 
    
    

def transform_geo(lat, lon):
    pass

def transform_town(town):
    pass

def transform_time(time):
    pass