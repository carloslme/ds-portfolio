import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es')
import dictionaries

def transform_day(date):
    #dt = '2021-07-08'
    # parsing date to datetime and extract day in Spanish
    year, month, day = (int(x) for x in date.split('-'))    
    ans = datetime.date(year, month, day)
    key = ans.strftime("%A").capitalize()
    print(key)

    # get key of day from data dictionary
    key = {k:dictionaries.days[k] for k in key if k in dictionaries.days}
    print(key)
    print(ans.strftime("%A").capitalize() in dictionaries.days)
    ''' mydict = {'one': 1, 'two': 2, 'three': 3}
    mykeys = ['three', 'one','ten']
    newList={k:mydict[k] for k in mykeys if k in mydict}
    print (newList)
    {'three': 3, 'one': 1}'''
    
    

def transform_geo(lat, lon):
    pass

def transform_town(town):
    pass

def transform_time(time):
    pass