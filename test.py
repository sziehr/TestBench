import requests
import json
import calendar
from datetime import date
from _datetime import timedelta, datetime
holdTemp = 0
holdDegreeDays = 0
city = 'Nashville'
state ='TN'
url = ''

def main():
    CurrentDate()
    print(holdTemp)
    print(holdDegreeDays)
    mydate = date.today()
    test33 = mydate - timedelta(1)
    capture = calendar.day_name[mydate.weekday()]  
    capture2 = calendar.day_name[test33.weekday()]
    print(capture)
    print(capture2)
                 
def CurrentDate():
    todaydate =date.today()
    DateCreator(todaydate)
    
def DateCreator(date):
    mydate = date.today()
    todaysName = calendar.day_name[mydate.weekday()]
    yesterday = mydate - timedelta(1)
    yesterdayName = calendar.day_name[yesterday.weekday()]
    
    # This portion of the code grabs the last day and prepares it for the url
    workingDate = date - timedelta(1)
    yesterdayYear = '20' + workingDate.strftime('%y')
    yesterdayDay = workingDate.strftime('%d')
    yesterdayMonth = workingDate.strftime('%m')
    urlCreator(yesterdayDay, yesterdayMonth, yesterdayYear, city, state)
    
def urlCreator (day, month, year, city, state):
    combinedDate = year + month + day
    urlString = ('htp://api.wunderground.com/api/4ed4d4b887e23593/history_{}/q/{}/{}.json'.format(combinedDate,state, city ))
    url = urlString
    GetData(url)
    print(url)
def GetData (url):
    jsonDatat = requests.get(url)
    print(jsonDatat.status_code)
    weatherData = jsonDatat.json()
    if not weatherData:
        print('error')
    else:
        ParseEnginge(weatherData)
        
def ParseEnginge (data):
    keyedDataExtraction = data['history']['dailysummary']
    for items in keyedDataExtraction:
        global holdDegreeDays
        global holdTemp 
        holdTemp = items['meantempi']
        holdDegreeDays =(items['coolingdegreedays'])
        
def RowSeek():
    pass

def PlaceinXl():
    pass

main()

