import sqlite3
from sqlite3 import Error
from daydiff import find,get_weather

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