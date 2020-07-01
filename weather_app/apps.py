from flask import Flask,render_template,request
import requests
import datetime
from datetime import datetime
import sqlite3
from sqlite3 import Error

app = Flask(__name__,template_folder="template",static_folder="static")

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

#To convert kelvin to celcius
def celsius(temp):
    return (round(float(temp) - 273.16,2))


def conn(city):
    #this function is to create connection to database and create a table in it
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS weather (city text, description text, temp integer, Time real)")
    sqliteConnection.commit()
    return sqliteConnection


def update(sqliteConnection,update_details):
    #this function is to update the details in db
    cursor = sqliteConnection.cursor()
    update_query = """Update weather set description =?,temp=?,Time=? where city = ?"""
    cursor.execute(update_query,(update_details[1],update_details[2],update_details[3],update_details[0]))
    sqliteConnection.commit()
    print("updated ") 


def insert(sqliteConnection,insert_details):
    #it is to insert new values into db
    cursor = sqliteConnection.cursor()
    insert_query="""INSERT INTO weather(city,description,temp,Time) VALUES(?, ?, ?, ?)"""
    cursor.execute(insert_query, insert_details)
    sqliteConnection.commit()
    print(" Inserted ")
   
def get(sqliteConnection,city):
    cursor = sqliteConnection.cursor()
    # it is to select the  details of defined city name given by the user
    get_query = """SELECT * from weather where city=?"""
    cursor.execute(get_query,[city])
    data= cursor.fetchall()
    #if city name exists in db
    if len(data):
        for elements in data:
            data=list(elements)
        day=find(data)
        #if day exist
        if day:
            #to get current weather details using function 
            update_details=get_weather(city)
            update(sqliteConnection,update_details)
            return update_details
        #not exist
        else:
            print("Exist")
            return data
    #if city is not exist
    else:
        #get weather details 
        insert_details=get_weather(city)
        insert(sqliteConnection,insert_details)
        return insert_details

      
#to get location weather detail in url
def get_weather(city):
    url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=c8df8e14215a96fe54fb8ef6b96dd189"
    json_response=requests.get(url).json()
    weather_description=json_response["weather"][0]["description"]
    temp=json_response["main"]["temp"]
    timestamp=datetime.now()
    return [city,weather_description,temp,timestamp]

@app.route("/")
def index():
    return render_template("first.html")


@app.route("/result",methods =['POST', 'GET'])
def weather():
    if request.method == 'POST':
      location = request.form['city'].lower()
      if location:
        sqliteConnection=conn(location)
        details=get(sqliteConnection,location)# gives details of location from db
        temp=celsius(details[2])
        print({"city":details[0],"Weather description":details[1],"temp(in k)":details[2],"temp(in C)":temp})
        return render_template('second.html',city=details[0],description=details[1],tempk=details[2],tempc=temp,time=details[3]) 
      else:
        return "<h1> City Name <h1> <a href=\"/\"> Home</a>"

if __name__ == '__main__':
   app.run(debug = True)