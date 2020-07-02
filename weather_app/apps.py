from flask import Flask,render_template,request
import datetime
from datetime import datetime
from base import conn,get


app = Flask(__name__,template_folder="template",static_folder="static")



#To convert kelvin to celcius
def celsius(temp):
    return (round(float(temp) - 273.16,2))


    


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