import requests
import json
from datetime import date
from _datetime import timedelta
holdTemp = 0
holdDegreeDays = 0
city = 'Nashville'
state ='TN'
url = ''

def main():
    CurrentDate()
    print(holdTemp)
    print(holdDegreeDays)
    
def CurrentDate():
    todaydate =date.today()
    DateCreator(todaydate)
    
def DateCreator(date):
    workingDate = date - timedelta(1)
    yesterdayYear = '20' + workingDate.strftime('%y')
    yesterdayDay = workingDate.strftime('%d')
    yesterdayMonth = workingDate.strftime('%m')
    urlCreator(yesterdayDay, yesterdayMonth, yesterdayYear, city, state)
    
def urlCreator (day, month, year, city, state):
    combinedDate = year + month + day
    urlString = ('http://api.wunderground.com/api/4ed4d4b887e23593/history_{}/q/{}/{}.json'.format(combinedDate,state, city ))
    url = urlString
    GetData(url)
    
def GetData (url):
    jsonDatat = requests.get(url)
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

def PlaceinXl(htemp, hdegreeday):
    pass

main()

