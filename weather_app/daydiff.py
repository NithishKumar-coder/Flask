import requests
import datetime
from datetime import datetime


def find(data):         
    difference=check_update(data[3])
    return check_day(difference)

def check_day(difference):
    if difference:
        return True   
    else :
        return False

#To find the difference of time in database  and current time
def check_update(time):
    time_in_data = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
    now_datetime=datetime.now()
    difference=now_datetime-time_in_data
    secs = difference.total_seconds()
    day=int((secs / 3600)/24)
    return day
    
#to get location weather detail in url
def get_weather(city):
    url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=c8df8e14215a96fe54fb8ef6b96dd189"
    json_response=requests.get(url).json()
    weather_description=json_response["weather"][0]["description"]
    temp=json_response["main"]["temp"]
    timestamp=datetime.now()
    return [city,weather_description,temp,timestamp]